import pytest
from Warmup.birthday_cake_candles import birthday_cake_candles


def _5_candles():
    """height of 5 candles"""
    return [82, 67, 10, 10, 1]

def _18_candles():
    """height of 18 candles"""
    return [19, 7525, 6348, 7264, 2333459, 3777, 2282, 9, 1196, 1359, 7526,
         7526, 6885045, 283, 7072, 1351, 96, 5726, 357, 422, 3777, 7525, 6885045]

def _100_candles():
    """height of 100 candles"""
    return [100] * 100

def answer(candles, height):
    sorted(height)
    count_max = height.count(max(height[candles // 2:-1]))
    return count_max

@pytest.mark.parametrize("candles, height, expected", [
    (len(_5_candles()), _5_candles(), 1),
    (len(_18_candles()), _18_candles(), 2),
    (len(_100_candles()), _100_candles(), 100),
])
def test_birthday_candles(candles, height, expected):
    assert birthday_cake_candles(candles, height) == expected

def test_birthday_candles_zero():
    with pytest.raises(ValueError):
        assert birthday_cake_candles(len([0]), [0]) == answer(len([0]), [0])

