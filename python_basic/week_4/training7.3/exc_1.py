import re

sentence = input("please write your sentence: ")

no_special_marks = re.sub(r"[^\w\s]", "", sentence)
print(no_special_marks)

sentence_reverse = list(sentence)[::-1]
print(sentence_reverse)
