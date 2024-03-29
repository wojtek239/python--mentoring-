import string

text = (
       "The quick brown fox jumps over the lazy dog is an English-language pangram—a "
       "sentence that contains all of the letters of the English alphabet"
)


# translator = str.maketrans('', '', string.punctuation)
# text = text.translate(translator)
# 
# words = text.split()

length_of_words = [
       len(word)
       for word in text.split(' ')
       if word.lower() != "the"
]

# length_of_words = [len(word) for word in words if word.lower() != "the"]

print(length_of_words)
