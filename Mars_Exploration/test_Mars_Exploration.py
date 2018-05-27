import pytest
from .Mars_Exploration import mars_exploration


@pytest.mark.parametrize("string, expected", [
    ("SOSSPSSQSSOR", 3),
    ("S" * 66, 22),
    ("SP1FGJKL74DFGWERTSOSSS34", 20),
    ("SOS", 0),
    ([0, 1, 2], 3),
])
def test_mars_exploration(string, expected):
    assert mars_exploration(string) == expected


def test_mars_exploration_fail():
    with pytest.raises(IndexError):
        assert mars_exploration(" ") == 0
