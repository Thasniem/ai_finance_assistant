"""
Backend package initializer.
Ensures all submodules are recognized as part of the backend package.
"""
import os
import sys

# Ensure the backend directory is in the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

