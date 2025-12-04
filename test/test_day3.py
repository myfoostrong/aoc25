import pytest

from days.day3 import star1, star2, example_input


class TestDay3:
    def test_star1_example_input(self):
        """Make sure we solve for the example"""
        assert star1(example_input) == 357

    def test_star2_example_input(self):
        """Make sure we solve for the example"""
        assert star2(example_input) == 3121910778619