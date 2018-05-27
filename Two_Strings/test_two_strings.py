import pytest
from .Two_Strings import two_strings


@pytest.mark.parametrize("s1, s2, common",[
("hello", "world", "YES"),
("hi", "world", "NO"),
("abcr45", "qweeryuopmh4fghj5", "YES"),
("a", " ", "NO"),
])
def test_two_strings(s1, s2, common):
    assert two_strings(s1, s2) == common

def test_fail_two_strings():
    with pytest.raises(TypeError):
        assert two_strings(1, 2) == "NO"

