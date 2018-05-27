import pytest
from .Ice_Cream_Parlor import ice_cream_parlor


def _2_flavours():
    return [300, 500]

def _5_flavours():
    return [1, 4, 5, 3, 2]

def _7_flavours():
    return [4510, 2808, 9204, 5369, 6028, 2852, 4211]

def _29_flavours():
    return [1372, 219, 6348, 3804, 9249, 7205, 8390,
            8447, 8228, 1712, 4409, 8554, 5482,
            249, 9833, 6217, 9746, 5600, 5291,
            3099, 9909, 5525, 6931, 2716, 5629,
            6604, 1202, 1219, 2801]

@pytest.mark.parametrize("flavours, money, expected",[
    (_2_flavours(), 800, (1, 2)),
    (_5_flavours(), 4, (1, 4)),
    (_29_flavours(), 8430, (25, 29))
  ])
def test_ice_cream_parlor(flavours, money, expected):
    assert ice_cream_parlor(flavours, money) == expected

