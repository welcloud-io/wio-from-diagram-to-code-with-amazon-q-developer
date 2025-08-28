#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
from unittest.mock import patch, mock_open, MagicMock
from build_tutorials_page import (
    tutorial_title, prerequisites, tutorial_starting_point, tutorial_prompts,
    tutorial_results, create_tutorial_section, empty_target_file, write_target_file,
    get_tutorial_title, tutorials_index, tutorials_section, build_tutorials_page,
    check_orphans, check_screenshot_dead_links
)


class TestBuildTutorialsPage(unittest.TestCase):

    def test_tutorial_title(self):
        props = {'title': 'Test Tutorial'}
        result = tutorial_title(props, 1)
        expected = ['## 1. Test Tutorial', '']
        self.assertEqual(result, expected)

    def test_prerequisites(self):
        result = prerequisites()
        expected = ['### [=> PREREQUISITES](../README.md#prerequisites)', '']
        self.assertEqual(result, expected)

    def test_tutorial_starting_point(self):
        props = {'starting_point': ['arg1', 'arg2']}
        result = tutorial_starting_point(props)
        expected = [
            "### Script to execute In VS Code terminal ('_playground/vscode-app-folder/')",
            '```',
            '../init-playground.sh arg1 arg2',
            '```',
            ''
        ]
        self.assertEqual(result, expected)

    def test_tutorial_prompts(self):
        props = {'prompts': ['prompt1', 'prompt2']}
        result = tutorial_prompts(props)
        expected = [
            '### Prompts to execute In Q Desktop, Q CLI, Kiro, ...',
            '```',
            'prompt1',
            '```',
            '```',
            'prompt2',
            '```',
            ''
        ]
        self.assertEqual(result, expected)

    def test_tutorial_results(self):
        props = {'result_example': ['./screenshots/test-image.png']}
        result = tutorial_results(props)
        expected = [
            '### Result Example',
            '![test image](./screenshots/test-image.png)',
            ''
        ]
        self.assertEqual(result, expected)

    def test_create_tutorial_section(self):
        tutorial_data = {
            'tutorial': {
                'title': 'Test',
                'starting_point': ['arg1'],
                'prompts': ['test prompt'],
                'result_example': ['test.png']
            }
        }
        result = create_tutorial_section(tutorial_data, 1)
        self.assertIn('## 1. Test', result)
        self.assertIn('### [=> PREREQUISITES](../README.md#prerequisites)', result)

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

    @patch('builtins.open', new_callable=mock_open, read_data='tutorial:\n  title: Test Title')
    def test_get_tutorial_title(self, mock_file):
        result = get_tutorial_title('test.yaml')
        self.assertEqual(result, 'Test Title')

    @patch('build_tutorials_page.get_tutorial_title')
    def test_tutorials_index(self, mock_get_title):
        mock_get_title.side_effect = ['Title 1', 'Title 2']
        files = ['file1.yaml', 'file2.yaml']
        
        result = tutorials_index(files)
        
        expected = [
            '# Tutorial Index',
            '1. [Title 1](#1-title-1)',
            '2. [Title 2](#2-title-2)',
            ''
        ]
        self.assertEqual(result, expected)

    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_tutorials_section(self, mock_yaml, mock_file):
        mock_yaml.return_value = {
            'tutorial': {
                'title': 'Test',
                'starting_point': ['arg1'],
                'prompts': ['prompt'],
                'result_example': ['test.png']
            }
        }
        
        files = ['test.yaml']
        result = tutorials_section(files)
        
        self.assertIn('## 1. Test', result)

    @patch('build_tutorials_page.tutorials_section')
    @patch('build_tutorials_page.tutorials_index')
    @patch('build_tutorials_page.write_target_file')
    @patch('build_tutorials_page.empty_target_file')
    def test_build_tutorials_page(self, mock_empty, mock_write, mock_index, mock_section):
        mock_index.return_value = ['index']
        mock_section.return_value = ['section']
        
        files = ['test.yaml']
        build_tutorials_page(files, 'output.md')
        
        mock_empty.assert_called_once_with('output.md')
        mock_write.assert_called_once_with('output.md', ['index', 'section'])

    @patch('os.listdir')
    def test_check_orphans(self, mock_listdir):
        mock_listdir.return_value = ['file1.yaml', 'file2.yaml', 'main-index.yaml']
        tutorial_files = ['tutorials/file1.yaml']
        
        result = check_orphans(tutorial_files)
        
        expected = ['file2.yaml']
        self.assertEqual(result, expected)

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_check_screenshot_dead_links(self, mock_yaml, mock_file, mock_exists):
        mock_yaml.return_value = {
            'tutorial': {
                'result_example': ['existing.png', 'missing.png']
            }
        }
        mock_exists.side_effect = lambda path: path == 'existing.png'
        
        files = ['test.yaml']
        result = check_screenshot_dead_links(files)
        
        expected = [('missing.png', 'test.yaml')]
        self.assertEqual(result, expected)

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    @patch('yaml.safe_load')
    def test_check_screenshot_dead_links_no_examples(self, mock_yaml, mock_file, mock_exists):
        mock_yaml.return_value = {'tutorial': {}}
        
        files = ['test.yaml']
        result = check_screenshot_dead_links(files)
        
        self.assertEqual(result, [])


    def test_generate_tutorials_md_output(self):

        tutorial_files = [
            'tutorials/tutorial-mermaid-architecture-diagram-from-code.yaml'
        ]

        target_file = 'TUTORIALS-TEST.md'

        build_tutorials_page(tutorial_files, target_file)
        
        with open(target_file, 'r') as f:
            content = f.read()
        
        expected_content = """# Tutorial Index
1. [Generate Mermaid Architecture Diagram from Code - Feedback App](#1-generate-mermaid-architecture-diagram-from-code---feedback-app)

## 1. Generate Mermaid Architecture Diagram from Code - Feedback App

### [=> PREREQUISITES](../README.md#prerequisites)

### Script to execute In VS Code terminal ('_playground/vscode-app-folder/')
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid architecture diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
```

### Result Example
![mermaid architecture diagram from code](./screenshots/mermaid-architecture-diagram-from-code.png)

"""
        
        actual_lines = content.splitlines()
        expected_lines = expected_content.splitlines()
        
        for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines)):
            self.assertEqual(actual, expected, f"Line {i+1} differs:\nActual:   '{actual}'\nExpected: '{expected}'")
        
        self.assertEqual(len(actual_lines), len(expected_lines), 
                        f"Different number of lines: actual={len(actual_lines)}, expected={len(expected_lines)}")

if __name__ == '__main__':
    unittest.main()