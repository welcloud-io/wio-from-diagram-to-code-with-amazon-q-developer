#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
from build_tutorials_page import build_tutorials_page

class TestGenerateTutorials(unittest.TestCase):
    
    def test_generate_tutorials_md_output(self):

        tutorial_files = [
            'tutorials/tutorial-mermaid-generate-architecture-diagram-from-code.yaml'
        ]

        build_tutorials_page(tutorial_files)
        
        with open('TUTORIALS.md', 'r') as f:
            content = f.read()
        
        expected_content = """# Tutorial Index
1. [Generate Flow Diagram](#generate-flow-diagram)

## Generate Flow Diagram

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