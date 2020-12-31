import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root, topdown=True):
        for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


album_list = find_albums("music", "Aerosmith")
song_list = find_songs(album_list)
# for a in album_list:
#     print(a)
# print("-" * 40)
for b in song_list:
    print(b)
