import main
def test_find_min_max():
    result = []
    input_list = [5, 57, 32]
    test_list = [5, 57]

    result = main.find_min_max(input_list)
    assert(result == test_list)

def test_calc_average():
    result = []
    input_list = [1, 2, 3, 4, 5]
    test_no = 3

    result = main.calc_average(input_list)
    assert(result == test_no)

def test_calc_median():
    result = []
    input_list = [1, 2, 3, 4, 5]
    test_no = 3

    result = main.calc_median(input_list)
    assert(result == test_no)
