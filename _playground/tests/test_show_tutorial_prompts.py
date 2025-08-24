#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
import sys
import re
from io import StringIO
from show_tutorial_prompts import show_tutorial_prompts

class TestShowTutorialPrompts(unittest.TestCase):
    
    # def setUp(self):
    #     # Create temporary file to put test data in
    #     self.test_dir = tempfile.mkdtemp()
    #     self.original_cwd = os.getcwd()
    #     os.chdir(self.test_dir)
        
    #     # Create test TUTORIALS.yaml
    #     test_data = {
    #         'Tutorial_1': {
    #             'Title': 'Generate MERMAID Diagrams from code',
    #             'Tutorial': {
    #                 'Starting_Point': ['--with-starting-point-folder=feedback-app-code'],
    #                 'Prompts': ['generate a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)'],
    #                 'Result_Example': ['../screenshots/mermaid-flow-diagram.png']
    #             }
    #         }
    #     }
        
    #     with open('TUTORIALS.yaml', 'w') as f:
    #         yaml.dump(test_data, f)
    
    # def tearDown(self):
    #     os.chdir(self.original_cwd)
    
    def test_show_tutorial_prompts_output(self):
        # Capture stdout
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            show_tutorial_prompts('TUTORIALS.yaml')
        finally:
            sys.stdout = original_stdout
        
        output = captured_output.getvalue()
        
        # Remove ANSI color codes for comparison
        output_clean = re.sub(r'\033\[[0-9;]*m', '', output)
        
        expected_output = """## TUTORIALS:

## Generate MERMAID Diagrams from code
> generate a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)

"""
        
        self.assertEqual(output_clean, expected_output)

if __name__ == '__main__':
    unittest.main()