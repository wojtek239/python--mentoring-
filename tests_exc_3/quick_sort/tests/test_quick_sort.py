from quick_sort import quick_sort


def test_empty_list():
    assert quick_sort([]) == []


def test_single_element_list():
    assert quick_sort([1]) == [1]


def test_sorted_list():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted_list():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_list_with_duplicated_numbers():
    assert quick_sort([3, 2, 2, 1, 3]) == [1, 2, 2, 3, 3]

    
def test_list_with_negative_numbers():
    assert quick_sort([-5, 0, -3, 3, 1]) == [-5, -3, 0, 1, 3]