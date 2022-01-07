from flask import Flask, request, render_template
import ml_model.model_learning as model_learning

app = Flask(__name__)
# Contiens toutes les ressources pour l'interface web (css, image...)
app.static_folder = 'static'

# Liste des genres supportés par le modèle de prédiction
GENRES = ['electro', 'metal', 'reggae', 'trap', 'k-pop', 'gospel', 'hip-hop', 'jazz']

def get_result(lyrics="", predict_genre=""):
    """Formate les données obtenues pour être envoyer"""
    res = {}
    res["lyrics"] = lyrics
    res["predict_genre"] = predict_genre
    res["genres"] = GENRES
    return res

@app.route("/")
def load_index(result=get_result()):
    """Load default page"""
    return render_template('index.html', result=result)

@app.route("/predict", methods=['POST'])
def predict():
    """Récupère les inputs pour prédire le genre"""
    lyrics = request.form["lyrics"]
    genre = ""

    if lyrics and lyrics != "":
        # formate l'input
        formated_lyrics = model_learning.format_lyrics(lyrics)
    
        # lance la prédiction
        genre = model_learning.predict([formated_lyrics])

        if genre is None:
            genre = ""
        
        genre = genre.capitalize()

    # Nous conservons les paroles brutes dans le formulaire et non les paroles formater
    res = get_result(lyrics=lyrics, predict_genre=genre)
    return load_index(res)

if __name__ == "__main__":
    app.run()