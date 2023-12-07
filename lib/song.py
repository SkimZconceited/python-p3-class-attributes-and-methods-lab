class Song:
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.genres.add(genre)
        Song.artists.add(artist)
        Song.count += 1

        # Update genre_count and artist_count
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            print(f"{cls.genre_count[genre]} that line for genre '{genre}'")

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            print(f"{cls.artist_count[artist]} that line for artist '{artist}'")
