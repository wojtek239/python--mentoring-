import re
import string

sentence = input("please type your sentence: ")

for sign in string.punctuation:
    phrase = phrase.replace(sign, "")


sentence_without = re.sub(r"[^\w\s]", "", sentence)
print(sentence_without)

words_ammount = len(sentence.split())
print(f"ammount of words in this sentence is: ", words_ammount)

words = sentence.split()
words_in_one_line = " ".join(words)
print(words_in_one_line)

first_word = words[0]
fourth_word = words[3]
print(f"first word is: ", first_word)
print(f"fourth word is: ", fourth_word)

special_words = set(sentence.split())
ammount_speial_words = len(special_words)
print(f"ammount of special words in this sentence is: ", ammount_speial_words)

special_words_one_line = " ".join(special_words)
print(special_words_one_line)

first_word1 = list(special_words)[-1]
fourth_word1 = list(special_words)[3]
print(f"first word is ", first_word1, "and fourth word is: ", fourth_word1)

if first_word1 == fourth_word1:
    print("they are the same")
else:
    print("they are not the same")
