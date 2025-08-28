#!/usr/bin/env python3

import unittest

import re

from show_tutorial_prompts import tutorial_prompts

class TestShowTutorialPrompts(unittest.TestCase):
        
    def test_show_tutorial_prompts_output(self):

        filtered_list_of_files = [
            'tutorials/tutorial-mermaid-architecture-diagram-from-code.yaml'
        ]
        
        content = tutorial_prompts(filtered_list_of_files[0])
        
        output = '\n'.join(content)

        # Remove ANSI color codes for comparison
        output_clean = re.sub(r'\033\[[0-9;]*m', '', output)
        
        expected_output = """## Generate Mermaid Architecture Diagram from Code - Feedback App
> create a mermaid architecture diagram of my application (data flow from up to bottom, use colors, keep formatting simple)

└──────────────────────────────────────────────────┘
"""

        # Compare text line by line for more granular test failure info
        expected_lines = expected_output.splitlines()
        actual_lines = output_clean.splitlines()
        for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines)):
            self.assertEqual(actual, expected, f"Line {i+1} differs:\nExpected: {expected}\nActual: {actual}")        
if __name__ == '__main__':
    unittest.main()