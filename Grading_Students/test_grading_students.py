import pytest
from .Grading_Students import grading_students as gs

@pytest.mark.parametrize("grades, expected",[
    ([73, 67, 38, 33], "75\n67\n40\n33\n"),
    ([95, 37, 101, 81, 76], "95\n37\n101\n81\n76\n"),
    ([0], "0\n")
])
def test_apple_orange(grades, expected, capsys):
    gs(grades)
    out, err = capsys.readouterr()
    assert out == expected



