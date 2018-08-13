import pytest
from .Apple_Orange import count_apples_and_oranges as ao


@pytest.mark.parametrize("s, t, a, b, apples, oranges, expected",[
    (7, 11, 5, 15, [-2, 2, 1], [5, -6], "1\n1\n"),
    (7, 11, 5, 15, [-5, -5], [-15], "0\n0\n"),
    (1, 3, 0, 5, [-10, -20], [40, 100], "0\n0\n"),
    (100, 200, 99, 201, [3, 5], [40, -98], "2\n1\n"),
])
def test_apple_orange(s, t, a, b, apples, oranges, expected, capsys):
    ao(s, t, a, b, apples, oranges)
    out, err = capsys.readouterr()
    assert out == expected



