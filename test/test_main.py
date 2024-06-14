"""Test main module."""

from main import sum_two_numbers


def test_sum_two_numbers():
    """Test sum_two_numbers function."""
    assert sum_two_numbers(1, 2) == 3
    assert sum_two_numbers(-1, 5) == 4
    assert sum_two_numbers(0, 0) == 0
    assert sum_two_numbers(3.14, 2.71) == 5.85
    assert sum_two_numbers(-10, -5) == -15
