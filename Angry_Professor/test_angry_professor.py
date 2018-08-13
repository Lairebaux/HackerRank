import pytest
from .Angry_Professor import angry_professor



@pytest.mark.parametrize("k, a, expected",[
    (3, [-1, -3, 4, 2], "YES"),
    (2, [0, -1, 2, 1], "NO"),
    (1, [0], "NO")
])
def test_counting_sort_1(k, a, expected):
   assert angry_professor(k, a) == expected


