# #!/usr/bin/env python3


import io
import sys
import unittest
from dog import Dog


class TestDog(unittest.TestCase):
    def test_name_not_empty(self):
        """Prints "Name must be string between 1 and 25 characters." if empty string."""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog = Dog(name="")
        sys.stdout = sys.__stdout__
        self.assertIn("Name must be string between 1 and 25 characters.", captured_out.getvalue())

    def test_name_string(self):
        """Prints "Name must be string between 1 and 25 characters." if not string."""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog = Dog(name=123)
        sys.stdout = sys.__stdout__
        self.assertIn("Name must be string between 1 and 25 characters.", captured_out.getvalue())

    def test_name_under_25(self):
        """Prints "Name must be string between 1 and 25 characters." if string over 25 characters."""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog = Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        sys.stdout = sys.__stdout__
        self.assertIn("Name must be string between 1 and 25 characters.", captured_out.getvalue())

    def test_breed_not_in_list(self):
        """Prints "Breed must be in list of approved breeds." if not in breed list."""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog = Dog(breed="Human")
        sys.stdout = sys.__stdout__
        self.assertIn("Breed must be in list of approved breeds.", captured_out.getvalue())


if __name__ == "__main__":
    unittest.main()
