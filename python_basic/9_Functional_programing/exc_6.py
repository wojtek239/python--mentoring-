colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
combine_tuples = lambda tpl: ' '.join(tpl)
result = list(map(combine_tuples, colors))
print(result)
