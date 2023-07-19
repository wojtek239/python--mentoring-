lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']
double_ones = lambda line: line.count('11') == 0
filtered_lines = list(filter(double_ones, lines))
count = len(filtered_lines)
print(f'lines with double ones are: ', count)

