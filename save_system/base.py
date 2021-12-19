import pickle


class SaveSystem:
    def __init__(self, path):
        self.path = path

    def save(self, datas):
        pass

    def load(self):
        return None


class PickleSaveSystem(SaveSystem):
    def __init__(self, path="corpus.pkl"):
        super().__init__(path)

    def save(self, datas):
        with open(self.path, "wb") as f:
            pickle.dump(datas, f)

    def load(self):
        with open(self.path, "rb") as f:
            return pickle.load(f)
