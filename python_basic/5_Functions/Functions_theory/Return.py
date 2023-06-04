import statistics as st

def get_data(list):
    arithmetic_mean = st.mean(list)
    standard_deviation = st.stdev(list)

    return arithmetic_mean, standard_deviation
#   return[arithmetic_mean, standard_deviation]

numbers = [1, 2, 3]
print(get_data(numbers))
