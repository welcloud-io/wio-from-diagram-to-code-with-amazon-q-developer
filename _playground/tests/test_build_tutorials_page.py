#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
from unittest.mock import patch, mock_open, MagicMock
from build_tutorials_page import (
    empty_target_file, write_target_file, TutorialIndex, TutorialSection,
    TutorialSections, TutorialPageBuilder, TutorialChecker
)


class TestBuildTutorialsPage(unittest.TestCase):

    def test_tutorial_section_title(self):
        with patch('builtins.open', mock_open(read_data='tutorial:\n  title: Test Tutorial\n  starting_point: [arg1]\n  prompts: [prompt1]\n  result_example: [test.png]')):
            section = TutorialSection('test.yaml', '1')
            self.assertIn('## 1. Test Tutorial', section.content)

    def test_tutorial_section_prerequisites(self):
        with patch('builtins.open', mock_open(read_data='tutorial:\n  title: Test\n  starting_point: [arg1]\n  prompts: [prompt1]\n  result_example: [test.png]')):
            section = TutorialSection('test.yaml', '1')
            self.assertIn('#### [=> Install Prerequisites](../README.md#prerequisites)', section.content)

    def test_tutorial_section_starting_point(self):
        with patch('builtins.open', mock_open(read_data='tutorial:\n  title: Test\n  starting_point: [arg1, arg2]\n  prompts: [prompt1]\n  result_example: [test.png]')):
            section = TutorialSection('test.yaml', '1')
            self.assertIn('../init-playground.sh arg1 arg2', section.content)

    def test_tutorial_section_prompts(self):
        with patch('builtins.open', mock_open(read_data='tutorial:\n  title: Test\n  starting_point: [arg1]\n  prompts: [prompt1, prompt2]\n  result_example: [test.png]')):
            section = TutorialSection('test.yaml', '1')
            self.assertIn('prompt1', section.content)
            self.assertIn('prompt2', section.content)

    def test_tutorial_section_results(self):
        with patch('builtins.open', mock_open(read_data='tutorial:\n  title: Test\n  starting_point: [arg1]\n  prompts: [prompt1]\n  result_example: [./screenshots/test-image.png]')):
            section = TutorialSection('test.yaml', '1')
            self.assertIn('![test image](./screenshots/test-image.png)', section.content)

    def test_empty_target_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write('existing content')
            tmp_name = tmp.name
        
        empty_target_file(tmp_name)
        
        with open(tmp_name, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, '')
        os.unlink(tmp_name)

    def test_write_target_file(self):
        content = ['line1', 'line2', 'line3']
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp_name = tmp.name
        
        write_target_file(tmp_name, content)
        
        with open(tmp_name, 'r') as f:
            result = f.read()
        
        expected = 'line1\nline2\nline3'
        self.assertEqual(result, expected)
        os.unlink(tmp_name)

    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_tutorial_index_get_title(self, mock_yaml, mock_file):
        mock_yaml.side_effect = [
            {'tutorial_index': [{'index_section': {'index_section_name': 'Section 1', 'indexed_tutorials': ['file1.yaml']}}]},
            {'tutorial': {'title': 'File 1 Title'}},
            {'tutorial': {'title': 'Test Title'}}
        ]
        index = TutorialIndex()
        result = index.get_tutorial_title('test.yaml')
        self.assertEqual(result, 'Test Title')

    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_tutorial_index(self, mock_yaml, mock_file):
        mock_yaml.side_effect = [
            {
                'tutorial_index': [
                    {'index_section': {'index_section_name': 'Section 1', 'indexed_tutorials': ['file1.yaml']}},
                    {'index_section': {'index_section_name': 'Section 2', 'indexed_tutorials': ['file2.yaml']}}
                ]
            },
            {'tutorial': {'title': 'Title 1'}},
            {'tutorial': {'title': 'Title 2'}}
        ]
        
        index = TutorialIndex()
        
        expected = [
        '# Tutorial Index',
        '',
        '1. [Section 1](#1-section-1)',
        '',
        '    - 1.1 [Title 1](#11-title-1)',
        '',
        '2. [Section 2](#2-section-2)',
        '',
        '    - 2.1 [Title 2](#21-title-2)',
        ''
        ]
        self.assertEqual(index.content, expected)

    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_tutorial_sections(self, mock_yaml, mock_file):
        mock_yaml.side_effect = [
            {'tutorial_index': [{'index_section': {'index_section_name': 'Section 1', 'indexed_tutorials': ['file1.yaml']}}]},
            {'tutorial': {'title': 'Test', 'starting_point': ['arg1'], 'prompts': ['prompt'], 'result_example': ['test.png']}}
        ]
        
        sections = TutorialSections()
        
        self.assertIn('## 1.1. Test', sections.content)

    @patch('builtins.open', new_callable=mock_open, read_data='tutorial_index: []')
    @patch('build_tutorials_page.empty_target_file')
    @patch('build_tutorials_page.write_target_file')
    def test_tutorial_page_builder(self, mock_write, mock_empty, mock_file):
        builder = TutorialPageBuilder('output.md')
        builder.build()
        
        mock_empty.assert_called_once_with('output.md')
        mock_write.assert_called_once()

    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    @patch('os.listdir')
    def test_check_orphans(self, mock_listdir, mock_yaml, mock_file):
        mock_listdir.return_value = ['file1.yaml', 'file2.yaml', 'main-index.yaml']
        mock_yaml.return_value = {
            'tutorial_index': [
                {'index_section': {'indexed_tutorials': ['file1.yaml']}}
            ]
        }
        
        checker = TutorialChecker()
        
        # Verify file2.yaml is identified as orphan
        self.assertIn('tutorial-descriptions/file1.yaml', checker.tutorial_files)
        self.assertNotIn('tutorial-descriptions/file2.yaml', checker.tutorial_files)

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_check_screenshot_dead_links(self, mock_yaml, mock_file, mock_exists):
        # Mock the main index file load
        mock_yaml.side_effect = [
            {'tutorial_index': [{'index_section': {'indexed_tutorials': ['test.yaml']}}]},
            {'tutorial': {'result_example': ['existing.png', 'missing.png']}}
        ]
        mock_exists.side_effect = lambda path: path == 'existing.png'
        
        checker = TutorialChecker()
        
        # The method doesn't return anything, it prints. We just verify it doesn't crash.
        checker.check_screenshot_dead_links()

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_check_screenshot_dead_links_no_examples(self, mock_yaml, mock_file, mock_exists):
        mock_yaml.side_effect = [
            {'tutorial_index': [{'index_section': {'indexed_tutorials': ['test.yaml']}}]},
            {'tutorial': {}}
        ]
        
        checker = TutorialChecker()
        checker.check_screenshot_dead_links()


    @patch('build_tutorials_page.TutorialSections')
    @patch('build_tutorials_page.TutorialIndex')
    @patch('build_tutorials_page.empty_target_file')
    @patch('build_tutorials_page.write_target_file')
    def test_generate_tutorials_md_output(self, mock_write, mock_empty, mock_index_class, mock_sections_class):
        mock_index = MagicMock()
        mock_index.content = ['# Tutorial Index']
        mock_index_class.return_value = mock_index
        
        mock_sections = MagicMock()
        mock_sections.content = ['## 1.1. Test']
        mock_sections_class.return_value = mock_sections

        target_file = 'TUTORIALS-TEST.md'
        builder = TutorialPageBuilder(target_file)
        builder.build()
        
        self.assertEqual(builder.target_file, target_file)
        self.assertIsNotNone(builder.content)

if __name__ == '__main__':
    unittest.main()