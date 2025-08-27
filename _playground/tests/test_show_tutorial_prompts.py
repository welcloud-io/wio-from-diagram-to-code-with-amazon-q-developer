#!/usr/bin/env python3

import unittest

import re

from show_tutorial_prompts import build_tutorial_prompts
from show_tutorial_prompts import display_format

class TestShowTutorialPrompts(unittest.TestCase):
        
    def test_show_tutorial_prompts_output(self):

        filtered_list_of_files = [
            'tutorials/tutorial-mermaid-generate-architecture-diagram-from-code.yaml'
        ]
        
        content = build_tutorial_prompts(filtered_list_of_files)
        
        output = display_format(content)

        # Remove ANSI color codes for comparison
        output_clean = re.sub(r'\033\[[0-9;]*m', '', output)
        
        expected_output = """## TUTORIALS:

## Generate Flow Diagram
> generate a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
"""

        self.assertEqual(output_clean, expected_output)

if __name__ == '__main__':
    unittest.main()