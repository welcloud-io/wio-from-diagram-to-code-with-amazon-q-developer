#!/usr/bin/env python3
import unittest
import tempfile
import os
import yaml
import re
from unittest.mock import patch, mock_open
from show_tutorial_prompts import (
    set_green,
    files_related_to_tutorial_configuration,
    tutorial_prompts,
    terminal_formated_prompts_related_to_tutorial_configuration
)

class TestShowTutorialPrompts(unittest.TestCase):

    def test_set_green(self):
        """Test ANSI color formatting"""
        result = set_green("test")
        self.assertEqual(result, "\033[32mtest\033[0m")

    def test_files_related_to_tutorial_configuration(self):
        """Test filtering tutorial files by configuration"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test tutorial files
            tutorial1_data = {
                'tutorial': {
                    'starting_point': ['config1', 'config2']
                }
            }
            tutorial2_data = {
                'tutorial': {
                    'starting_point': ['config3']
                }
            }
            
            with open(f"{temp_dir}/tutorial1.yaml", 'w') as f:
                yaml.dump(tutorial1_data, f)
            with open(f"{temp_dir}/tutorial2.yaml", 'w') as f:
                yaml.dump(tutorial2_data, f)
            
            result = files_related_to_tutorial_configuration(temp_dir, 'config1')
            self.assertEqual(len(result), 1)
            self.assertTrue(result[0].endswith('tutorial1.yaml'))

    def test_tutorial_prompts(self):
        """Test extracting prompts from tutorial file"""
        tutorial_data = {
            'section1': {
                'title': 'Test Title',
                'prompts': ['prompt1', 'prompt2']
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(tutorial_data, f)
            temp_file = f.name
        
        try:
            result = tutorial_prompts(temp_file)
            self.assertIn("\033[32m## Test Title\033[0m", result)
            self.assertIn("> prompt1", result)
            self.assertIn("> prompt2", result)
        finally:
            os.unlink(temp_file)

    @patch('show_tutorial_prompts.files_related_to_tutorial_configuration')
    @patch('show_tutorial_prompts.tutorial_prompts')
    def test_terminal_formated_prompts_related_to_tutorial_configuration(self, mock_tutorial_prompts, mock_files_related):
        """Test terminal formatting of prompts"""
        mock_files_related.return_value = ['file1.yaml']
        mock_tutorial_prompts.return_value = ['## Test', '> prompt']
        
        result = terminal_formated_prompts_related_to_tutorial_configuration('test_folder', 'test_config')
        
        self.assertIn("┌" + "─" * 50 + "┐", result)
        self.assertIn("\x1b[32m## TUTORIALS:\x1b[0m", result)
        self.assertIn("## Test", result)
        self.assertIn("> prompt", result)
        self.assertIn("└" + "─" * 50 + "┘", result)

    def test_output_with_real_file(self):

        filtered_list_of_files = [
            'tutorials/tutorial-mermaid-architecture-diagram-from-code.yaml'
        ]
        
        content = tutorial_prompts(filtered_list_of_files[0])
        
        output = '\n'.join(content)

        # Remove ANSI color codes for comparison
        output_clean = re.sub(r'\033\[[0-9;]*m', '', output)
        
        expected_output = """## Generate Mermaid Architecture Diagram from Code - Feedback App
> create a mermaid architecture diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
"""

        # Compare text line by line for more granular test failure info
        expected_lines = expected_output.splitlines()
        actual_lines = output_clean.splitlines()
        for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines)):
            self.assertEqual(actual, expected, f"Line {i+1} differs:\nExpected: {expected}\nActual: {actual}")        

if __name__ == '__main__':
    unittest.main()