colours = input("Wprowadź 5 kolorów oddzielonych przecinkami: ")
divided_colours = colours.split(',')
# aby rozdzielic na pojedyncze słowa
print(divided_colours)
print("trzeci kolor to: ", divided_colours[2])
# tutaj po prostu wybiera 3 wyraz, pisac 2 bo liczymy od zera