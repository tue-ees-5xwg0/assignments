
from unittest.mock import patch
import unittest

# --- Code to test ---

def multiply(x, y):
    print("Actually multiplying...")  # Simulate side effect
    return x * y

def double(x):
    return multiply(x, 2)

def triple(x):
    return multiply(x, 3)

# --- Tests ---

class TestMathOps(unittest.TestCase):

    @patch("__main__.multiply")
    def test_double(self, mock_multiply):
        mock_multiply.return_value = 10
        result = double(5)
        self.assertEqual(result, 10)
        mock_multiply.assert_called_once_with(5, 2)

    @patch("__main__.multiply")
    def test_triple(self, mock_multiply):
        mock_multiply.return_value = 12
        result = triple(4)
        self.assertEqual(result, 12)
        mock_multiply.assert_called_once_with(4, 3)

if __name__ == "__main__":
    unittest.main()