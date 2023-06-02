
text = """
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of someone gently rapping, rapping at my chamber door.
This visitor, I muttered, tapping at my chamber door -
Only this, and nothing more.
"""
word_count = {}
words = text.split()

for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
