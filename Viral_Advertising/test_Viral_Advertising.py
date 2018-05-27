import pytest
from .Viral_Advertising import viral_advertising

@pytest.mark.parametrize("n , expected", [
    (1, 2),
    (2, 5),
    (5, 24),
    (25, 81938),
    (40, 35875988),
    (50, 2068789129)
    ])
def test_viral_advertising(n, expected):
    assert viral_advertising(n) == expected




