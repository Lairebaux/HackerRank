import pytest
from .Chocolate_feast import chocolate_feast


@pytest.mark.parametrize("n, c, m, expected", [
    (6, 2, 2, 5),
    (10, 2, 5, 6),
    (12, 4, 4, 3),
    (2, 3, 3, 0)
])
def test_chocolate_feast(n, c, m, expected):
    assert chocolate_feast(n, c, m,) == expected

