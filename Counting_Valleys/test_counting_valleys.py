import pytest
from .Counting_Valleys import counting_valleys as cv



@pytest.mark.parametrize("n, s, expected",[
    (8, "UDDDUDUU", 1),
    (2, "UU", 0),
    (1, "U", 0),
    (6, "UUUDDD", 0),
    (8, "DDUUUUDD", 1),
    (31, "DDUUUUDDUDUDUDUDUDUDDDDUUDUDDUU", 1),
    (24, "DDUUUUDDDDUUDDUUUUDDDDUU", 4)
])
def test_counting_valleys(n, s, expected):
    assert cv(n, s) == expected

