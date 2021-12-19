from models.corpus import SongCorpus
from save_system.base import PickleSaveSystem

DB_PATH = "./databases/database-scrap.pkl"

def main():
    corpus = SongCorpus("Genius Lyrics")

    # Charge la base de données
    pickleStream = PickleSaveSystem(DB_PATH)
    songs = pickleStream.load()

    # Ajoute les musiques aux corpus
    for song in songs:
        corpus.add(song)

    # print("\nGet Documents By Type")
    # print(corpus.get_documents_by_type("TestingSong"))

    # print("\nSearch")
    # print(corpus.search("Machine"))

    # print("\nConcorde")
    # print(corpus.concorde("Machine", 5))

    # print("\nStats")
    # corpus.stats(corpus.get_all_text(), 5)

    # print("\nSearch by genre")
    # print(len(corpus.search_songs_by_genre("pop")))

    # print("\nStats in pop")
    # pop_songs = corpus.get_text_by_genre("pop")
    # print(corpus.stats(pop_songs, 5))



if __name__ == "__main__":
    main()
