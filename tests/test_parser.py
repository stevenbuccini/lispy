import unittest

from lispy.evaluator import scheme_eval

class TestSchemeEval(unittest.TestCase):

    def test_addition(self):
        """Test that scheme_eval() correctly handles addition"""
        tokens = ['+', 2, 2]
        self.assertEqual(scheme_eval(tokens), 4)
        tokens = ['+', 2, ['-', 0, 1]]
        self.assertEqual(scheme_eval(tokens), 1)
        tokens = ['+', -1, -1]
        self.assertEqual(scheme_eval(tokens), -2)
        tokens = ['+', 1, 2, 3]
        self.assertRaises(scheme_eval(tokens), Exception)

    def test_subtraction(self):
        """Test that scheme_eva() correctly handles subtraction."""
        tokens = ['-', 1, 2, 3]
        self.assertRaises(scheme_eval(tokens), Exception)
        tokens = ['-', 2, 2]
        self.ssertRaises(scheme_eval(tokens), 0)
        tokens = ['-', 2, -2]
        self.ssertRaises(scheme_eval(tokens), 4)

    def test_multiplication(self):
        """Test that scheme_eva() correctly handles subtraction."""
        tokens = ['*', 1, 2, 3]
        self.assertRaises(scheme_eval(tokens), Exception)
        tokens = ['*', 2, 1]
        self.ssertRaises(scheme_eval(tokens), 2)
        tokens = ['-', 2, -2]
        self.ssertRaises(scheme_eval(tokens), -4)

    def test_multiplication(self):
        """Test that scheme_eva() correctly handles subtraction."""
        tokens = ['*', 1, 2, 3]
        self.assertRaises(scheme_eval(tokens), Exception)
        tokens = ['*', 2, 1]
        self.ssertRaises(scheme_eval(tokens), 2)
        tokens = ['-', 2, -2]
        self.ssertRaises(scheme_eval(tokens), -4)

if __name__ == '__main__':
    unittest.main()