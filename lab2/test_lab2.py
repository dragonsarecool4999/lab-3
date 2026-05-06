import lab2.main as main
import pytest

def test_min_max():
    result = []
    input_arr = [99,67,68,69,41]
    result = main.calc_min_max_temperature(input_arr)
    answer = [41,99]
    assert(result==answer)
def test_calc_average():
    result = []
    input_arr = [21,727,69,420,41,67]
    result = main.calc_average_temperature(input_arr)
    assert result == pytest.approx(224.166666, rel=1e-3)
def test_calc_median_temperature():
    result = []
    input_arr = [65,66,67,68,69]
    result = main.calc_median_temperature(input_arr)
    assert result == 67