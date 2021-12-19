class Song:
    """Définie une musique (extraite, apprentissage...)"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def get_type(self):
        return type(self).__name__
    
    def get_text(self):
        return self.lyrics

class TrainingSong(Song):
    def __init__(self, lyrics, genre):
        super().__init__(lyrics)
        self.genre = genre

class TestingSong(Song):
    def __init__(self, lyrics, genre, title, authors):
        super().__init__(lyrics)
        self.genre = genre
        self.title = title
        self.authors = authors
    
    def __str__(self):
        clean_authors = " - ".join(self.authors)
        return f"{self.title} create by {clean_authors}."
