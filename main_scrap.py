from scrappers.genius_scrapper import GeniusScrapper, FilterGeniusWithDocumentLength, CastGeniusDatas
from controllers.scrapper_controller import ScrapperController
from save_system.base import PickleSaveSystem

TOKEN = ""

# Nombre de page à charger => 1 page = 20 paroles
SCRAP_LIMIT = 51
MIN_LYRICS_LENGTH = 100
TAGS = [
    "rock",
    "pop",
    "country",
    "r-b",
    "hip-hop",
    "electro",
    "jazz",
    "blues",
    "classical-music",
    "metal",
    "reggae",
    "folk",
    "chill",
    "trap",
    "disco",
    "k-pop",
    "gospel",
    "techno",
    "indie"
]

EXPORT_PATH = "database-scrap.pkl"

def main():
    # All scrapping platform
    scrappers = [
        # Genius scrapper / Filter / Cast or format
        (GeniusScrapper(TOKEN),
         FilterGeniusWithDocumentLength(MIN_LYRICS_LENGTH),
         CastGeniusDatas())
    ]

    # Extrait les données pour chaque genre / tag
    songs = []
    scrapper_controller = ScrapperController(SCRAP_LIMIT, scrappers)
    for tag in TAGS:
        print(f"----------------- {tag} -----------------")
        songs += scrapper_controller.scrap_datas(tag)
        print(f"Nombre de paroles extraites : {len(songs)}")

    # Exporte le résultat
    pickleStream = PickleSaveSystem(EXPORT_PATH)
    pickleStream.save(songs)

if __name__ == "__main__":
    main()
