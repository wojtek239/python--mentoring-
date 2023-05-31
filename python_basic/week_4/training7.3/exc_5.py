import string

phrase = "Darkness comprise, on wishes The dream wheel propped with the star in Will stop the progress of the sky" \
         "Cause earth turns and drags us Into the heat The hardness of the shell of human aims The strength of melted " \
         "thoughts. Of' under, hands Elektronic? visions; of associations for time! into. back gear."


def remove_punctuation(sentence):
    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, "")
    return sentence


cleared_phrase = remove_punctuation(phrase)
print(f"phrase without punctuation is: ", cleared_phrase)


# ammount of words
words = phrase.split()
words_count = len(words)
print(f"ammount of words in this phrase is: ", words_count)

# capitalized words
capitalized_words = [word for word in words if word[0].isupper()]
if capitalized_words:
    print(f"capitalized words in this phrase are: ", capitalized_words)
else:
    print("there are no capitalized words")

# concrete words (like and, in, on, under, for)
search_words = ["and", "in", "on", "under", "for"]
found_words = [word for word in words if word in search_words]
if found_words:
    print(f"there are words like: ", found_words)
else:
    print("there are no such words")

# sort
sorted_words = words.sort
print(sorted_words)
