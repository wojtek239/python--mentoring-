music_albums = {
    "The Sensual World": "Kate Bush",
    "Shayday": "Ofra Haza",
    "Achtung Baby": "U2",
    "Aion": "Dead Can Dance",
    "Invisible Touch": "Genesis"
}
print("aviable albums: ")
for album in music_albums.keys():
    print(album)

user_input = input("please enter album name: ")
if user_input in music_albums:
    artist = music_albums[user_input]
    print(f"creator of ", {user_input}, "is", {artist})
else:
    print("no data")