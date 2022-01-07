# Import des packages
from save_system.base import PickleSaveSystem

# Package préparation des données
import pandas as pd
import string
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Création du modèle / répartition des apprentissages
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# Modèle de prédiction des chansons
MODEL_FILE_PATH = "ml_model/model-svm.sav"

def format_lyrics(lyrics):
    # Enlève la partie embed venant du scrapping de genius
    lyrics = lyrics.replace('EmbedShare URLCopyEmbedCopy','')

    # Suppresion des crochets / annotations des paroles ex : [Verse]
    all_lines = lyrics.split("\n")
    lyrics = ""
    for one_line in all_lines:
        if "[" not in one_line:
            lyrics += one_line + " "

    # Passage sous forme de liste
    corpus = lyrics.split('delimiter')
    # Passage en minuscule
    corpus = [doc.lower() for doc in corpus]

    # Retrait des ponctuations
    ponctuations = list(string.punctuation)
    corpus = ["".join([char for char in list(doc) if not (char in ponctuations)]) for doc in corpus]

    # Retrait des chiffres
    corpus = [re.sub(r'\d+', '', doc) for doc in corpus]

    corpus_tk = [word_tokenize(doc) for doc in corpus]

    # Lemmatisation 
    lem = WordNetLemmatizer()
    corpus_lem = [[lem.lemmatize(mot) for mot in doc] for doc in corpus_tk]

    stop_words = stopwords.words('english')

    # Retrait des stopwords
    corpus_st = [[mot for mot in doc if not mot in stop_words] for doc in corpus_lem]
    # Retrait des mots inf à 3
    corpus_st = [[mot for mot in doc if len(mot) >=3] for doc in corpus_st]


    for i in range(0, len(corpus_lem)):
       clean_lyrics = ' '.join(corpus_st[i])

    return clean_lyrics

def predict(lyrics):
    """Prédit le genre d'une chanson à partir de ses paroles"""
    res = ""
    # Charge le modèle de prédiction
    pickleStream = PickleSaveSystem(MODEL_FILE_PATH)
    model = pickleStream.load()
    res = model.predict(lyrics)

    if len(res) == 0:
        return None

    return res[0]