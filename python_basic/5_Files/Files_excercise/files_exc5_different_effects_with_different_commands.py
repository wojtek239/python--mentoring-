with open("example.txt", encoding="utf-8") as file:
    file.tell() #--> pokazuje aktualna pozycje wskaźnika na pliku
    file.seek(43)  #--> ustawia pozycje wskaźnika pliku na 43
    print(file.read(1)) #--> odczytuje i wyswietla 1 znak z pliku
