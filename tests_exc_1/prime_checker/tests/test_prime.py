import pytest
from tests_exc_1.prime_checker.prime_function import is_prime
# from ..prime_function import is_prime


@pytest.mark.parametrize(
    'number',
    [-1, -7, -5, -25]
)
def test_should_return_false_for_negative_values(number):
    assert not is_prime(number)

# dłuzsze opisy
def test_zero_and_one():
    assert not is_prime(0)
    assert not is_prime(1)


def test_prime_numbers():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)


def test_non_prime_numbers():
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(9)
    assert not is_prime(10)
