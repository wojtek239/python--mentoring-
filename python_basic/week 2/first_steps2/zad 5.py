text = '     wefwefwfw fdwfwfwef      '
# tylko z lewej mi wychodzi stripowanie
print(text)

text_without_whitespaces_left = text.lstrip()
text_without_whitespaces_right = text.rstrip()
text_without_whitespaces_both = text.strip()

print(text_without_whitespaces_left)
print(text_without_whitespaces_right)
print(text_without_whitespaces_both)
print(text.replace(" ", ""))
