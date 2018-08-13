import pytest
from .Diagonal_Difference import diagonal_difference as df




@pytest.mark.parametrize("a, expected",[
    ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
    ([[-99, -98, -97], [0, 50, 56], [66, 13, 22]], 46),
])
def test_apple_orange(a,expected):
    assert df(a) == expected

