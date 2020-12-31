class Song:
    """ Class to represent a song

    Args:
        title (str): title of the song
        artist (str): name of the songs creator
        duration (Optional [int]): duration of the song
    """

    def __init__(self, title, artist, duration=0):
        self.artist = artist
        self.title = title
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent the Album, using it's track list

    Attributes:
        name (str): name of the album
        year (int): year which album was introduced
        artist (str): name of artist responsible for te album
        tracks (List[Song]): list of songs in the album

    Methods:
        add_song: used to add new song in the album
    """

    def __init__(self, name, year, artist):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds Song to the list

        :param song: A song to add
        :param position : if specified song will be added to that position
                in the track list - inserting between the songs else at end
        :return: void method
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store the artist details

    Attributes:
        name(str): name of the artist
        albums(List[Album]): ablums of the artist

    Methods:
        add_album: Used to add an album to the artist
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Used to add album to the artist

        :param album: album to add to artist
        :return:
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """ add the song to the respective album of artist and if album
         doesn't exist create a new album and add it

        :param name: name of album
        :param year: year of album
        :param title: title of the song
        :return:
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Album found" + name)

        album_found.add_song(title)


# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
# Song.__init__.__doc__ = """ Updated Song init method
#
#         Args:
#             title (str): title of the song
#             artist (Artist: artist object creating the song represented
#             duration (Optional [int]): duration of the song
#         """
# help(Song.__init__.__doc__)

def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(artist, album, song), file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    create_checkfile(artists)
