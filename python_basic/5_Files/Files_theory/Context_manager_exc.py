def count_words():
    ammount_of_words = 0
    with open("example.txt", "r") as file:
        for line in file.readlines():
            words = line.split()
            ammount_of_words += len(words)
    return ammount_of_words

def main():
    print(f"ammount of words in file is {count_words()}")


if __name__ == "__main__":
    main()