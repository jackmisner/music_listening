class Album():
    def __init__(self, artist, album, song_list):
        self.artist = artist
        self.album = album
        self.song_list = song_list
        self.album_dict = {album:song_list}

    def __repr__(self):
        return f"Artist: {self.artist}, Album: {self.album}, Songs: {'; '.join(self.song_list)}"
