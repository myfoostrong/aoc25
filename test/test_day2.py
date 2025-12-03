import pytest

from days.day2 import star1, star2, get_range


class TestDay2:
    def test_example_input(self):
        """Make sure we solve for the example"""
        example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

        assert star1(example_input) == 1227775554

    def test_get_range(self):
        assert get_range("95","115") == ("95", "99")
        assert get_range("998", "1012") == ("1000", "1012")
        assert get_range("1234", "12345") == ("1234", "9999")

    def test_edge_cases(self):
        assert star1("11-22,99-99") == 132
        