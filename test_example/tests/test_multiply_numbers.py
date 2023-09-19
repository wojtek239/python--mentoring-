import pytest
from test_example.functionality.multiply_numbers import multiply_numbers


def test_should_return_0_for_non_arguments_given():
    expected_result = 0
    actual_result = multiply_numbers()

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "expected_result, number",
    [
        (1, 1), (-3, -3), (20, 20)
    ]
)
def test_should_return_the_same_number_given_in_one_element_list(expected_result,
                                                                 number):
    actual_result = multiply_numbers(number)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "expected_result, numbers",
    [
        (6, [1, 2, 3]),
    ]
)
def test_should_return_correct_sum_for_few_numbers(expected_result, numbers):
    actual_result = multiply_numbers(*numbers)

    assert actual_result == expected_result
