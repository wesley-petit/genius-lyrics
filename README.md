# genius-lyrics

Ce projet fait partie des modalités d’évaluations de la Programmation Python du Master 1 Informatique à l’Université Lumière Lyon 2 pour l’année 2021 - 2022. 


Description du dépôt git : 
- main_summary.py, fichier de création du corpus à partir des données extraites du scrapping 
- main_scrap.py, fichier d'extraction des données sur Genius pour la préparation du modèle 
- main_server.py, fichier permettant d'afficher l'interface web et réalise la prédiction du genre à partir des paroles

Lien pour obtenir une clé d'extraction TOKEN dans le fichier main_scrap.py : https://docs.genius.com/#/getting-started-h1

Dans le cas d'une erreur avec l'installation du package nltk : https://www.nltk.org/install.html

python -m nltk.downloader punkt
nltk.download('punkt')
