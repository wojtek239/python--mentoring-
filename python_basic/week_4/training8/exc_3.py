# petle zagniezdzone czy intertools do generowania mozliwych permutaccji 2 ze tylko dwa elementy
import itertools

family_members = ["Adam", "Stanislaw", "Kornelia", "Joanna", "Wojtek"]
possible_combinations = list(itertools.permutations(family_members, 2))

for person1, person2 in possible_combinations:
    print(f"{person1} gives best wishes to {person2}")
