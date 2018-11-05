# Functional test
#
# Run it with `python3 -m unittest -v test_hello.py`

import unittest
import os
import subprocess
from pathlib import Path

class TestHello(unittest.TestCase):
    def test_hello(self):
        result = subprocess.run("./hello", capture_output=True)
        self.assertEqual(result.stdout.decode("utf-8"), "Hello, dear world!\nHello, people!\n")
