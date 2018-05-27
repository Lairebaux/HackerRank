import pytest
from .Breaking_the_Records import breaking_records


def scores_2():
    return [10, 5, 20, 20, 4, 5, 2, 25, 1]

def scores_4():
    return [7181, 2358, 1454, 7429]

def scores_7():
    return [45106505, 28084351, 92045116, 53695454, 60282844, 28525153, 42112051]


@pytest.mark.parametrize("scores, expected",[
    (scores_2(), (2, 4)),
    (scores_4(), (1, 2)),
    (scores_7(), (1, 1)),
    ([0] * 5, (0, 0))
])
def test_breaking_records(scores, expected):
    assert breaking_records(scores) == expected

@pytest.mark.parametrize("scores, expected",[
    (scores_2(), (3, 4)),
    (scores_4(), (1, 10005)),
    (scores_7(), (1123, 1)),
    ([0] * 5, (1, 1))
])
def test_fail_breaking_records(scores, expected):
    assert breaking_records(scores) != expected
