music_albums = {
    'The Sensual World': 'Kate Bush',
    'Shaday': 'Ofra Haza',
    'Achtung Baby': 'U2',
    'Aion': 'Dead Can Dance',
    'Invisible Touch': 'Genesis'
}
while True:
    print("\n--- MENU --- \n 1. display aviable albums \n 2. add new album \n 3. delete album \n 0. end program")

    choice = input("please select number from 0 to 3")
    if choice == 1:
        print("aviable albums: ")
        for album in music_albums.keys():
            print(album)
    elif choice == 2:
        album_name = input("please enter new album name: ")
        artist_name = input("please enter new artist name: ")
        music_albums[album_name] = artist_name
        print(f"you added", album_name, "by", artist_name)
    elif choice == 3:
        album_name = input("please enter album name to delete: ")
        if album_name in music_albums:
            del music_albums[album_name]
            print(f"you have deleted", album_name)
        else:
            print("there is no such album here")
    elif choice == 0:
        break
    else:
        print("wrong number")
