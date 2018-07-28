import pytest
from .electronics_shop import get_money_spent


@pytest.mark.parametrize("k, d, b, expected", [
    ([3, 1], [5, 2, 8], 10, 9),
    ([4], [5], 5, -1)
])
def test_get_money_spent(k, d, b, expected):
    assert get_money_spent(k, d, b) == expected



