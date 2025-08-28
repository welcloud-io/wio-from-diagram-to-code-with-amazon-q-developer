#!/usr/bin/env python3

import unittest
import tempfile
import os
import yaml
from build_tutorials_page import build_tutorials_page

class TestGenerateTutorials(unittest.TestCase):
    
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

### Make sure you have installed the [prerequisites](../README.md#prerequisites)

### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid architecture diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
```

### Result Example
![mermaid architecture diagram from code](../screenshots/mermaid-architecture-diagram-from-code.png)

"""
        
        actual_lines = content.splitlines()
        expected_lines = expected_content.splitlines()
        
        for i, (actual, expected) in enumerate(zip(actual_lines, expected_lines)):
            self.assertEqual(actual, expected, f"Line {i+1} differs:\nActual:   '{actual}'\nExpected: '{expected}'")
        
        self.assertEqual(len(actual_lines), len(expected_lines), 
                        f"Different number of lines: actual={len(actual_lines)}, expected={len(expected_lines)}")

if __name__ == '__main__':
    unittest.main()