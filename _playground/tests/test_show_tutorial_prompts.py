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
        
    def test_show_tutorial_prompts_output(self):
        # Capture stdout
        captured_output = StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            show_tutorial_prompts('./tutorials', '--with-starting-point-folder=feedback-app-code')
        finally:
            sys.stdout = original_stdout
        
        output = captured_output.getvalue()
        
        # Remove ANSI color codes for comparison
        output_clean = re.sub(r'\033\[[0-9;]*m', '', output)
        
        expected_output = """## TUTORIALS:

## Generate Flow Diagram
> generate a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)

## Generate Sequence Diagram
> generate a mermaid sequence diagram of the application

"""
        
        self.assertEqual(output_clean, expected_output)

if __name__ == '__main__':
    unittest.main()