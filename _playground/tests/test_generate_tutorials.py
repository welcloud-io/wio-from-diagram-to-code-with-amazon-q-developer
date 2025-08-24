#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
from generate_tutorials import generate_tutorials_md

class TestGenerateTutorials(unittest.TestCase):
    
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
    
    def test_generate_tutorials_md_output(self):
        generate_tutorials_md()
        
        with open('TUTORIALS.md', 'r') as f:
            content = f.read()
        
        expected_content = """# Tutorial Index

1. [Generate Application/Flow Diagram](#generate-application/flow-diagram)

## Generate Application/Flow Diagram

### Initialize Tutorial (In VS Code tutorial window terminal)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```
### Write Prompt (In Q Desktop, Q CLI, Kiro, ...)


```
generate a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
```


### Result Example

![mermaid flow diagram](../screenshots/mermaid-flow-diagram.png)
"""
        
        actual_lines = content.splitlines()
        expected_lines = expected_content.splitlines()
        
        for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines)):
            self.assertEqual(actual, expected, f"Line {i+1} differs:\nActual:   '{actual}'\nExpected: '{expected}'")
        
        self.assertEqual(len(actual_lines), len(expected_lines), 
                        f"Different number of lines: actual={len(actual_lines)}, expected={len(expected_lines)}")

if __name__ == '__main__':
    unittest.main()