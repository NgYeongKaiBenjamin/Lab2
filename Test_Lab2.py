import Lab2

print("Test Lab2")


def test_find_min_max():
    result = []
    input_arr = [10, 20, 40, 9, 35]
    result = Lab2.find_min_max(input_arr)
    assert (result == (9, 40))

def test_calc_average():
    result = []
    input_arr = [10, 20, 40, 15, 35]
    result = Lab2.calc_average(input_arr)
    assert (result == 24)

def test_calc_median_temperature():
    result = []
    input_arr = [10, 20, 40, 9, 35]
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == 20)
