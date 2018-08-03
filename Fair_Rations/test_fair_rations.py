import pytest
from .Fair_Rations import fair_rations



@pytest.mark.parametrize("B, expected",[
    ([2, 3, 4, 5, 6, 7], "NO"),
    ([11, 13, 15, 17, 19], "NO"),
    ([2, 4, 6, 8, 10], 0),
    ([3, 5, 6, 7, 8, 1, 20, 56, 77, 99], 8),
    ([0], 0),
    ([2, 3, 4, 5, 6], 4),
    ([99, 100, 101, 102, 103, 160, 167], 8)
])
def test_fair_rations(B, expected):
    assert fair_rations(B) == expected



