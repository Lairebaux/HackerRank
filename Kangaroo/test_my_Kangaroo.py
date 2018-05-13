import pytest
from my_Kangaroo import kangaroo


@pytest.mark.parametrize("x1, v1, x2, v2 , expected", [
    (0, 2, 5, 3, "NO"),
    (0, 3, 4, 2, "YES"),
    ])
def test_kangaroo(x1, v1, x2, v2, expected):
    assert kangaroo(x1, v1, x2, v2) == expected


