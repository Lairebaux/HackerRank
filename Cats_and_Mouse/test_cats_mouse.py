import pytest
from .Cats_Mouse import cats_and_mouse

@pytest.mark.parametrize("x, y, z, winner",[
        (4, 2, 3, "Mouse C"),
        (50, 65, 70, "Cat B"),
        (86, 3, 98, "Cat A"),
        (0, 1, 92, "Cat B"),
        (0, 0, 38, "Mouse C"),
        ])
def test_cats_and_mouse(x, y, z, winner):
    assert cats_and_mouse(x, y, z) == winner

