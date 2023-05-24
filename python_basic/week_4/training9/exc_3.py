#Mając poniższy słownik:
#dokonaj jego odwrócenia, tzn. niech wartości staną się kluczami, a klucze wartościami.
#Dla powyższego przykładu poprawnym wynikiem będzie:
#{3 : ‘a’, 1 : ‘b’, 10 : ‘c’, 15 : ‘d’, 20 : ‘e’}

dict = {"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
new_dict = {}
new_dict = {value: key for key, value in dict.items()}
print(new_dict)

#metoda items
