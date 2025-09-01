import os
import sys
import pytest

# Add the parent directory to the Python path so that we can import the lib module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))