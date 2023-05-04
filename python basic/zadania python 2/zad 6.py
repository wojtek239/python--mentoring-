kolory = input("Wprowadź 5 kolorów oddzielonych przecinkami: ")
rozdzielone_kolory = kolory.split(',')  #aby rozdzielic na pojedyncze słowa
print(rozdzielone_kolory)
print("trzeci kolor to: ", rozdzielone_kolory[2])   #tutaj po prostu wybiera 3 wyraz, pisac 2 bo liczymy od zera