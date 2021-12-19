class Author:
    """Author name and all his creations"""

    def __init__(self, name):
        self.name = name
        self.productions = []

    def add(self, songIndex):
        """Add a document created by the author"""
        if songIndex is not None:
            self.productions.append(songIndex)

    def __repr__(self):
        return f"{self.name} has created {len(self.productions)} documents."
