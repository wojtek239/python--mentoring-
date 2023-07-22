colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
combine_tuples = lambda color: ' '.join(color)

result = list(map(combine_tuples, colors))
# list(map(lambda color: f'color[0] color[1]', color))
print(result)
