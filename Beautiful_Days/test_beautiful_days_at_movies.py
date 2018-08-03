import pytest
from .Beautiful_Days_at_the_Movies import beautiful_days as bd


@pytest.mark.parametrize("i, j, k, expected",[
    (20, 23, 6, 2),
    (12, 13, 4, 0),
    (1, 6, 3, 5),
    (0, 0, 1, 0),
    (100, 122, 10 , 3)
])
def test_beautiful_days(i, j, k, expected):
    assert bd(i, j, k) == expected

