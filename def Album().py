def make_album(art_name, al_title, number_of_song=''):
    if number_of_song:
        album = {'artist_name': art_name, 'album_title': al_title, 'number of songs':number_of_song}
    else:
        album = {'artist_name': art_name, 'album_title': al_title}
    return album

album_info1 = make_album('prince','climb the mountain',5)
print(album_info1,"\n")

album_info2 = make_album('roshan','on the edge')
print(album_info2,"\n")

album_info3 = make_album('satyam','do something',6)
print(album_info3,"\n")