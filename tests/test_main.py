import unittest
from io import StringIO
import sys
from src import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        # Capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        main.main()  # Call the main function

        # Restore stdout
        sys.stdout = sys.__stdout__

        self.assertIn("Welcome to the Software-Defined Radio (SDR) project!", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
