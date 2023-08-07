def make_album(art_name, al_title):
    album = {'Artist' : art_name, 'Album' : al_title}
    return album

while True:
    prompt = "enter Artist Name & Album Title:\n"
    prompt += "('enter 'q' to exit at any time')"

    artist_name = input(f"Enter Artist Name:")
    if artist_name == 'q':
        break

    album_title = input(f"Enter Album Title:")
    if album_title == 'q':
        break

    album_01 = make_album(artist_name, album_title)
    print(album_01)