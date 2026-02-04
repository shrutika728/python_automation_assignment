import os
import sys

# ensure project root is on sys.path so tests can import top-level packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))