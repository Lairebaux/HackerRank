import pytest
from .Missing_Numbers import missing_numbers


@pytest.mark.parametrize("a, b, expected", [
    ("203 204 205 206 207 208 203 204 205 206",
     "203 204 204 205 206 207 205 208 203 206 205 206 204",
     [204, 205, 206]),
])
def test_circular_array_rotation(a, b, expected):
    assert missing_numbers(a, b) == expected
