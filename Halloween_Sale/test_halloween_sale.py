import pytest

from .Halloween_Sale import how_many_games as games



@pytest.mark.parametrize("p, d, m, s, expected", [
    (20, 3, 6, 80, 6),
    (20, 3, 6, 85, 7)
])
def test_how_many_games(p, d, m, s, expected):
    assert games(p, d, m, s) == expected

