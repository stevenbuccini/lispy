import pytest

from lispy.evaluator import scheme_eval

class TestSchemeEval:

    def test_addition(self):
        """Test that scheme_eval() correctly handles addition"""
        tokens = ['+', 2, 2]
        assert scheme_eval(tokens) == 4
        tokens = ['+', 2, ['-', 0, 1]]
        assert scheme_eval(tokens) ==  1
        tokens = ['+', -1, -1]
        assert scheme_eval(tokens) == -2


    def test_addition_too_many_args(self):
        """ Test that addition raises error if given too many args."""
        with pytest.raises(Exception):
            tokens = ['+', 1, 2, 3]
            scheme_eval(tokens)

    def test_subtraction(self):
        """Test that scheme_eva() correctly handles subtraction."""

        tokens = ['-', 2, 2]
        assert scheme_eval(tokens) == 0 
        tokens = ['-', 2, -2]
        assert scheme_eval(tokens) == 4

    def test_subtraction_exceptions(self):
        """ Test that subtraction throws errors in certain cases."""
        with pytest.raises(Exception):
            tokens = ['-', 1, 2, 3]
            scheme_eval(tokens)

    def test_multiplication(self):
        """Test that scheme_eva() correctly handles subtraction."""
        tokens = ['*', 2, 1]
        assert scheme_eval(tokens) == 2
        tokens = ['*', 2, -2]
        assert scheme_eval(tokens) == -4

    def test_multiplication_too_many_args(self):
        """Test that mult. raises error with too many args."""
        with pytest.raises(Exception):
            tokens = ['*', 1, 2, 3]
            scheme_eval(tokens)

    def test_division(self):
        """Test that scheme_eva() correctly handles division."""
        tokens = ['/', 2, 1]
        assert (scheme_eval(tokens) == 2)
        tokens = ['/', 2, -2]
        assert (scheme_eval(tokens) == -1)
