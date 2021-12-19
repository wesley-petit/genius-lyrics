from lyricsgenius import Genius
from models.song import TestingSong
from scrappers.base import Scrapper, ScrapperFilter, CastScrapperDatas


class GeniusScrapper(Scrapper):
    def __init__(self, token):
        # Initialise la connexion avec l'API
        self.genius = Genius(token, timeout=20, retries=30)
        # Enlève les annotions entre crochets pour les paroles (ex : [Chorus])
        self.genius.remove_section_headers = True
        # N'inclus pas les éléments de type playlist
        self.genius.skip_non_songs = True
        # Exclue les remix ou live du corpus
        self.genius.excluded_terms = ["(Remix)", "(Live)"]

    def scrap(self, query_terms, scrap_limit):
        """Récupère les paroles des musiques par genre"""

        # Code provenant de l'API de lyrics genius
        page = 1
        songs = []
        y = 0
        while page and page < scrap_limit:
            try:
                # Envoie la requête pour le tag
                res = self.genius.tag(query_terms, page=page)

                # Récupère les données pour chaque musique
                for hit in res['hits']:
                    # print(hit.keys())
                    hit["lyrics"] = self.genius.lyrics(song_url=hit['url'])
                    hit["genre"] = query_terms
                    songs.append(hit)
                    y += 1
                    print(y)
                page = res['next_page']
            except Exception as e:
                print(e)

        return songs


class FilterGeniusWithDocumentLength(ScrapperFilter):
    def __init__(self, min_document_length):
        """Filter datas that are below a given length"""
        self.min_document_length = min_document_length

    def is_filtered(self, raw_song):
        return super().is_empty_or_null(raw_song["lyrics"]) or len(raw_song["lyrics"]) < self.min_document_length


class CastGeniusDatas(CastScrapperDatas):
    def can_cast(self, raw_song):
        return raw_song

    def to_document(self, raw_song):
        if not self.can_cast(raw_song):
            return None
        
        return TestingSong(raw_song["lyrics"], raw_song["genre"], raw_song["title"], raw_song["artists"])
