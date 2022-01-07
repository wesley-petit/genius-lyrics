from models.song import TrainingSong
from models.corpus import SongCorpus
from save_system.base import PickleSaveSystem
import pandas as pd

DB_PATH = "./databases/database-scrap.pkl"

def main():    
    corpus = SongCorpus("Genius Lyrics")

    # Charge la base de données
    pickleStream = PickleSaveSystem(DB_PATH)
    songs = pickleStream.load()

    # Ajoute les musiques aux corpus
    for song in songs:        
        corpus.add(song)

    sum = 0
    for genre in corpus.genre_to_songs:
        sum += len(corpus.search_songs_by_genre(genre))
    
    print(f"Taille corpus : {sum}")
    print(f"Moyenne par genre : {sum / len(corpus.genre_to_songs)}")

    # # Préparation des données en csv 
    # genre = corpus.genre_to_songs
    # list_lyrics = []
    # list_genre = []
    # for i in genre :
    #     for j in corpus.search_songs_by_genre(i) :
    #         train_song = TrainingSong(j.get_text(), i)
    #         list_lyrics.append(train_song.lyrics)
    #         list_genre.append(train_song.genre)
        

    # df_global = pd.DataFrame({'lyrics': list_lyrics,
    #                'genre': list_genre})
    # df_global.to_csv('df_train.csv',index=False) 

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
