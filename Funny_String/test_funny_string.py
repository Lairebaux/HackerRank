import pytest
from .Funny_string import funny_string


@pytest.mark.parametrize("string, expected",[
    ("abc", "Funny"),
    ("acxz", "Funny"),
    ("bcxz", "Not Funny"),
    ("goddog", "Funny"),
    ("gg", "Funny"),
    ("dogood", "Not Funny"),
    ("abcdfg", "Not Funny"),
    (" ", "Funny")
])
def test_funny_string(string, expected):
    assert funny_string(string) == expected

