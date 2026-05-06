import lab2.bmi as bmi

def test_bmi_normal_weight():
    # Testing for a normal weight result
    result = bmi.calculate_bmi(weight=57, height=1.73)
    assert result == 0

def test_bmi_over_weight():
    # Testing for an overweight result
    result = bmi.calculate_bmi(weight=85, height=1.73)
    assert result == 1

def test_bmi_under_weight():
    # Testing for an underweight result
    result = bmi.calculate_bmi(weight=45, height=1.73)
    assert result == -1