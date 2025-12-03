import pytest

from days.day2 import star1, star2, example_input


class TestDay2:
    def test_star1_example_input(self):
        """Make sure we solve for the example"""
        assert star1(example_input) == 1227775554

    def test_star2_example_input(self):
        """Make sure we solve for the example"""
        assert star2(example_input) == 4174379265


    # def test_get_range(self):
    #     assert get_range("95","115") == ("95", "99")
    #     assert get_range("998", "1012") == ("1000", "1012")
    #     assert get_range("1234", "12345") == ("1234", "9999")

    def test_edge_cases(self):
        assert star1("11-22,99-99") == 132
        