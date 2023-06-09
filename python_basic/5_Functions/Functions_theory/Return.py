import statistics as st


def get_data(numbers: list[int]) -> tuple[int, float]:
    arithmetic_mean = st.mean(numbers)
    standard_deviation = st.stdev(numbers)

    return arithmetic_mean, standard_deviation
#   return[arithmetic_mean, standard_deviation]


numbers = [1, 2, 3]
print(get_data(numbers))
