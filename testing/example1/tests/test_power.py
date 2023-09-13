import pytest
from testing.example1.app.operations import calc_power


# def test_should_return_correct_value_for_positive_exp():
#     base = 3
#     exp = 3
#     expected_result = 27
#
#     actual_result = calc_power(base, exp)
#
#     assert actual_result == expected_result


@pytest.mark.parametrize(
    "base, exp, expected_result",
    [
        (3, 3, 27),
        (3, 2, 9),
        (5, 3, 125),
    ]
)
def test_should_return_correct_value_for_positive_exp(base, exp, expected_result):
    actual_result = calc_power(base, exp)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "base, exp, expected_result",
    [
        (2, -2, 0.25),
        (5, -2, 0.04),
        (2, -3, 0.125),
    ]
)
def test_should_return_correct_value_for_negative_exp(base, exp, expected_result):
    actual_result = calc_power(base, exp)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "exp",
    [
        20,
        0,
    ]
)
def test_should_return_0_for_0_base(exp):
    base = 0
    expected_result = 0

    actual_result = calc_power(base, exp)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "base",
    [
        -2,
        20,
        0,
    ]
)
def test_should_return_1_for_0_exp(base):
    exp = 0
    expected_result = 1

    actual_result = calc_power(base, exp)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "base, exp, expected_result",
    [
        (100, 0.5, 10),
        (32, 0.2, 2),
        (16, 0.25, 2),
    ]
)
def test_should_return_correct_float_value_for_fractional_exp(base, exp,
                                                              expected_result):
    actual_result = calc_power(base, exp)

    assert actual_result == expected_result
