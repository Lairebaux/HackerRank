import pytest
from String.Gemstones import gemstones


@pytest.mark.parametrize("string, common",[
(["abc", "rtyuiippabce", "56789abc", "rtqwerabc","ioplkjmabc"], 3),
(["abcdde", "baccd", "eeabg"], 2),
(["0sdfghj", "qewrtyuo0", "zxcv0bnm"], 1),
(["qwertyuiopasdfghjklzxcvvbnm", "qwertyuiopasdfghjklzxcvvbnm"], 26),
(["xxx", "qewrtyuo0", "zocv0bnm"], 0),
(["", "", ""], 0)
])
def test_gemstones(string, common):
    assert gemstones(string) == common

def test_gemstone_integer():
    with pytest.raises(TypeError):
        assert gemstones([1, 123, 4561]) == 1

