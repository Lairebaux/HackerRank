import pytest
from my_Time_Conversion import time_conversion


@pytest.mark.parametrize("AM_PM, military",[
    ("12:00:00AM", "00:00:00"),
    ("02:15:36AM", "02:15:36"),
    ("10:51:11AM", "10:51:11"),
    ("12:00:00PM", "12:00:00"),
    ("01:48:03PM", "13:48:03"),
    ("11:05:45PM", "23:05:45"),
    ])
def test_time_conversion(AM_PM, military):
    assert time_conversion(AM_PM) == military


if __name__ == '__main__':
	pytest.main()