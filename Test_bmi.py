import Lab2.bmi


def test_bmi_normal_weight():
    bmi_result = Lab2.bmi.calculate_bmi(1.73,57)
    if 18.5 < bmi_result & bmi_result <= 25.0:
        print("Normal Weight")

def test_bmi_over_weight():
    bmi_result = Lab2.bmi.calculate_bmi(1.73,57)
    if bmi_result > 25.0:
        print("Over Weight")

def test_bmi_under_weight():
    bmi_result = Lab2.bmi.calculate_bmi(1.73,57)
    if bmi_result < 25.0:
        print("Under Weight")
    