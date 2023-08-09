three_d = [
    [
        [1, 2, 3, 4],
        [0, -1, -2, -3, -4, -5, -6],
    ],
    [
        [1, 10, 15, 12, 20, 20, 20],
        [-15, -13, 14, 20, -1],
    ]
]
output = []
for lists in three_d:
    for inner in lists:
        if len(inner) > 4:
            output.append(inner)
print(output)

output2 = [
    inner
    for lists in three_d
    for inner in lists
    if len(inner) > 4
]
print(output2)

# [[0, -1, -2, -3, -4, -5, -6], [1, 10, 15, 1, 20, 20, 20], [-15, -13, 14, 20, -1]]