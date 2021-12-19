import re
import string
import pandas
from models.author import Author


class Corpus:
    def __init__(self, name):
        """Text corpus (articles, lyrics...)

        Args:
            name (string): corpus name
        """
        self.name = name
        self.authors = {}
        self.all_documents = []
        self.all_text = None

    def get_documents_by_type(self, search_type):
        return [d for d in self.all_documents if d.get_type() == search_type]

    def get_all_text(self):
        """Merge all text in each document

        Returns:
            string: merged text
        """
        if self.all_text is None:
            all_text = [d.get_text() for d in self.all_documents]
            self.all_text = " ".join(all_text)
        return self.all_text

    def add(self, doc):
        """Add a document in the corpus"""
        if doc is None:
            return

        # Add in the corpus
        self.all_documents.append(doc)
        currentIndex = self.all_documents.index(doc)

        # Add author infos
        for current_author in doc.authors:
            if current_author not in self.authors:
                self.authors[current_author] = Author(current_author)

            # Link documents and authors
            self.authors[current_author].add(currentIndex)

    def sort_by_title(self, n_docs):
        """Sort all documents by title

        Args:
            n_docs (int): Number of docs to display

        Returns:
            Array: All documents sorted
        """
        docs = list([v for v in self.all_documents if v.title])
        docs = list(sorted(docs, key=lambda x: x.title.lower()))[:n_docs]
        print(docs[1:5])
        return docs

    def search(self, query_words):
        all_text = self.get_all_text()
        return re.finditer(query_words, all_text)

    def concorde(self, query_words, context_size):
        patterns = self.search(query_words)
        datas = {'left_context': [], 'pattern': [], 'right_context': []}

        for pattern in patterns:
            start, end = pattern.span()

            datas["left_context"].append(
                self.all_text[start - context_size:start]
            )
            datas["pattern"].append(
                self.all_text[start:end]
            )
            datas["right_context"].append(
                self.all_text[end: end + context_size]
            )

        dataframe = pandas.DataFrame(data=datas)
        return dataframe

    def get_frequency(self, all_text):
        # List all words
        all_text = self.clean_text(all_text)
        all_words = all_text.split(" ")
        all_words = pandas.DataFrame(all_words, columns=["words"])
        unique_words = list(set(all_words["words"]))

        # Count term frequency
        frequency = all_words.value_counts()
        frequency = pandas.DataFrame(frequency, columns=["term_frequency"])

        # # Count document frequency for each word
        # frequency["document_frequency"] = 0
        # for i, current_frequency in enumerate(frequency.values):
        #     for doc in self.all_documents:
        #         if unique_words[i] in doc.get_text():
        #             current_frequency[1] += 1

        return frequency

    def stats(self, all_text, n_words):
        frequency = self.get_frequency(all_text)

        print("Corpus - " + self.name)

        num_words = len(all_text.split(" "))
        print("Nombre de mots : " + str(num_words))

        num_words = len(set(all_text.split(" ")))
        print("Nombre de mot différents : " +
              str(num_words))
        print(frequency.head(n_words))

    def clean_text(self, text):
        text = str(text).lower()
        text = text.replace("\n", "")

        # Remove punctuation
        regexp_punctuation = re.compile(
            "[" + re.escape(string.punctuation) + "]")
        text = re.sub(regexp_punctuation, "", text)

        # Remove number
        text = re.sub(r'\d+', "", text)
        return text

    def __repr__(self):
        # Sort all documents
        docs = self.sort_by_title(len(self.all_documents) - 1)
        return "\n".join(list(map(str, docs)))

class SongCorpus(Corpus):
    def __init__(self, name):
        super().__init__(name)
        self.genre_to_songs = {}
    
    def add(self, song):
        super().add(song)

        # Store all songs by genre
        if "genre" in song.__dict__:
            if song.genre not in self.genre_to_songs:
                self.genre_to_songs[song.genre] = []
            self.genre_to_songs[song.genre].append(song)

    def search_songs_by_genre(self, search_genre):
        """Search all songs by music genre"""
        if search_genre not in self.genre_to_songs:
            return None
        
        return self.genre_to_songs[search_genre]
    
    def get_text_by_genre(self, search_genre):
        """Merge all lyrics on a music genre"""
        songs = self.search_songs_by_genre(search_genre)

        if songs is None:
            return None

        all_text = [d.get_text() for d in list(songs)]
        return " ".join(all_text)