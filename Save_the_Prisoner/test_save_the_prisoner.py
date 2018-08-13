import pytest
from .Save_the_Prisoner import save_the_prisoner as sp


@pytest.mark.parametrize("n, s, m, expected",[
    (5, 2, 1, 2),
    (3, 3, 7, 3),
    (5, 2, 2, 3),
    (4, 6, 2, 3),
    (2, 1, 1, 1),
    (10, 1, 0, 10),
    (100, 100, 99, 98),
    (45689, 4000, 1245, 5244)
])
def test_save_the_prisoner(n, s, m, expected):
    assert sp(n, s, m) == expected
