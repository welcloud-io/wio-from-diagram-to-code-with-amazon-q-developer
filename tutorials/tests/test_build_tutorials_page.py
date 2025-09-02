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
    
    def test_tutorials_md_generation(self):
        tutorial_page_builder = TutorialPageBuilder('tests/fixtures/test-index.yaml')
        tutorial_page_builder.build('tests/fixtures/TUTORIALS-TEST-RESULT.md')

        # compare tests/fixtures/TUTORIALS-TEST-RESULT.md with tests/fixtures/TUTORIALS-TEST-EXPECTED.md line by line
        with open('tests/fixtures/TUTORIALS-TEST-RESULT.md', 'r') as f:
            result_lines = f.readlines()
            with open('tests/fixtures/TUTORIALS-TEST-EXPECTED.md', 'r') as f:
                expected_lines = f.readlines()
                self.assertEqual(len(result_lines), len(expected_lines), "Files have different number of lines")
                for i, (result_line, expected_line) in enumerate(zip(result_lines, expected_lines)):
                    self.assertEqual(result_line, expected_line, f"Line {i+1} differs:\nExpected: {expected_line}\nGot: {result_line}")

    def test_readme_md_generation(self):
        tutorial_page_builder = TutorialPageBuilder('tests/fixtures/test-index.yaml')
        tutorial_page_builder.update_readme_index(target_file='tests/fixtures/README-TEST-TO-MODIFY.md', tutorial_page='tutorials/TUTORIALS.md')

        # compare tests/fixtures/README-TEST-TO-MODIFY.md with tests/fixtures/README-TEST-EXPECTED.md line by line
        with open('tests/fixtures/README-TEST-TO-MODIFY.md', 'r') as f:
            result_lines = f.readlines()
            with open('tests/fixtures/README-TEST-EXPECTED.md', 'r') as f:
                expected_lines = f.readlines()
                self.assertEqual(len(result_lines), len(expected_lines), "Files have different number of lines")
                for i, (result_line, expected_line) in enumerate(zip(result_lines, expected_lines)):
                    self.assertEqual(result_line, expected_line, f"Line {i+1} differs:\nExpected: {expected_line}\nGot: {result_line}")

if __name__ == '__main__':
    unittest.main()
