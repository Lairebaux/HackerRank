import pytest
from .Kangaroo import kangaroo


@pytest.mark.parametrize("x1, v1, x2, v2 , expected", [
    (0, 2, 5, 3, "NO"),
    (0, 3, 4, 2, "YES"),
    (20, 3, 4, 2, "YES"),
    (569, 10000, 968, 1234, "NO"),
    (0, 9998, 0, 9999, "NO"),
    (459, 1, 862, 1, "NO"),
    ])
def test_kangaroo(x1, v1, x2, v2, expected):
    assert kangaroo(x1, v1, x2, v2) == expected


