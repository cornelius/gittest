# Functional test
#
# Run it with `python3 -m unittest -v test_hello.py`

import unittest
import os
import subprocess
from pathlib import Path

class TestHello(unittest.TestCase):
    def test_hello(self):
        hello = (Path(os.path.dirname(__file__)) / "hello").resolve()
        result = subprocess.run([hello], stdout=subprocess.PIPE)
        self.assertEqual(result.stdout.decode("utf-8"), "Hello, dear world!\nHello, people!\n")
