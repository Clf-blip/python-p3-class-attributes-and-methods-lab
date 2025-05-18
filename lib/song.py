class Song:
    pass


class Song:
    # - class attributes
    count = 0                       # total Song objects
    genres = []                     # every genre ever seen (duplicates removed)
    artists = []                    # every artist ever seen (duplicates removed)
    genre_count = {}                # {"Rap": 3, ...}
    artist_count = {}               # {"Jay Z": 2, ...}

    # ---------- instance initializer 
    def __init__(self, name: str, artist: str, genre: str):
        
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre not in Song.genres:
            Song.genres.append(genre)

        
        if artist not in Song.artists:
            Song.artists.append(artist)

        
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
