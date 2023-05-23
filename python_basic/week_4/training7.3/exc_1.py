sentence = input("please write your sentence: ")

import re
no_special_marks = re.sub(r"[^\w\s]", "", sentence)
print(no_special_marks)

sentence_list = list(sentence)

sentence_reverse = sentence[::-1]
print(sentence_reverse)

