music_albums = {
    'The Sensual World': 'Kate Bush',
    'Shaday': 'Ofra Haza',
    'Achtung Baby': 'U2',
    'Aion': 'Dead Can Dance',
    'Invisible Touch': 'Genesis'
}

MENU = (
    """
    --- MENU ---
    1. display aviable albums
    2. add new album
    3. delete album
    0. end program
"""
)

# choices = {
#     1: 'print_album',
#     2: 'add_album',
#     3: 'delete_album',
#     0: 'end',
# }
# choices.get(user_choice)

# while (choice := input(MENU)) != '0':
while True:
    choice = input(MENU)
    if choice == '1':
        print("aviable albums: ")
        for album in music_albums.keys():
            print(album)
    elif choice == '2':
        album_name = input("please enter new album name: ")
        artist_name = input("please enter new artist name: ")
        music_albums[album_name] = artist_name
        print(f"you added", album_name, "by", artist_name)
    elif choice == "3":
        album_name = input("please enter album name to delete: ")
        if album_name in music_albums:
            del music_albums[album_name]
            print(f"you have deleted", album_name)
        else:
            print("there is no such album here")
    elif choice == "0":
        break
    else:
        print("wrong number")
