import pytest
from .Caesar_Cipher import caesar_cipher



@pytest.mark.parametrize("string, k, expected",[
    ("abc", 2, "cde"),
    ("middle-Outz", 2, "okffng-Qwvb"),
    ("abcdefghijklmnopqrstuvwxyz", 8, "ijklmnopqrstuvwxyzabcdefgh"),
    ("ZjejinjKeljrOTadfT", 10, "JtotsxtUovtbYDknpD")
])
def test_next_day(string, k, expected):
    assert caesar_cipher(string, k) == expected

