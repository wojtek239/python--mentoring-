users_friends = input("please enter names of your friends divided by space pls: ").split()

for name in users_friends:
    print(f"hi {name}, how are you doing? ")
    print(f"haven't seen you in a long time {name} ")
    print(f"it's good to see you {name} ")


names = ["Bartosz", "Anna", "Kasia", "Marek"]
messages = ["Nice to meet you", "Welcome", "Have a nice day", "Hi"]

for name, message in zip(names, messages):
    print(f"{message} {name}")

