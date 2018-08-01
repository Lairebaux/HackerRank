import pytest
from .circular_array import circular_array_rotation as cr


@pytest.mark.parametrize("k, a, queries, expected", [
    (2, [1, 2, 3], [0, 0, 0], [2, 2, 2]),
    (3, [99, 10, 2, 3, 672], [0, 2, 3], [2, 672, 99]),
    (10, [], [], []),
    (1, [1, 2], [-1], [1]),
])
def test_circular_array_rotation(k, a, queries, expected):
    assert cr(a, k, queries) == expected
