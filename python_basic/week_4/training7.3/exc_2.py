import random


score = [12, 1, 45, 76, 50, 23]

for num in score:
    if not 1 <= num <= 49:
        new_num = random.randint(1, 49)
        print(f'inccorect number {num} replaced by {new_num}')
        score[score.index(num)] = new_num


print(score)

# mam to porównać?
