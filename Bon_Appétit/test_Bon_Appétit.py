import pytest
from .Bon_Appétit import bon_appetit


def _4_items():
    """list of 4 items"""
    return [3, 10, 2, 9]

def _5_items():
    """list of 5 items"""
    return [69152, 33947, 55002, 93043, 49474]

def _6_items():
    """list of 4 items"""
    return [3, 10, 2, 9]

def _8_items():
    """list of 8 items"""
    return [3, 3537, 1260, 385, 73096, 1000, 7747, 300]


@pytest.mark.parametrize("items, index, total, expected", [
    ([1, 1], 0, 1, 0),
    (_4_items(), 1, 12, 5),
    (_5_items(), 2, 122808, "Bon Appetit"),
    (_8_items(), 4, 0, 36548)
])
def test_bon_appetit(items, index, total, expected):
    assert bon_appetit(items, index, total) == expected


