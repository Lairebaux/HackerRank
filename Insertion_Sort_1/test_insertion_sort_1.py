import pytest
from .insertion_sort_1 import insertion_sort_1



@pytest.mark.parametrize("array, length, expected", [
    ([2, 4, 6, 8, 3],  5, "2 4 6 8 8\n2 4 6 6 8\n2 4 4 6 8\n2 3 4 6 8\n"),
    ([1, 2, 4, 5, 3],  5, "1 2 4 5 5\n1 2 4 4 5\n1 2 3 4 5\n"),
    ])
def test_insertion_sort_1(length, array, expected, capsys):
    insertion_sort_1(length, array)
    out, err = capsys.readouterr()
    assert out == expected


