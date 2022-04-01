from flask import Blueprint
from flask import render_template, request, make_response
from controllers import animauxController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
animaux_bp = Blueprint('animaux_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pageAnimaux', methods=['GET'])
def pageAnimaux():
    animaux_data=animauxController.getAnimaux()
    for animaux in animaux_data:
        print(animaux.famille_id, animaux.sexe, animaux.presence, animaux.apprivoise, animaux.mort_ne, animaux.decede)
    return render_template("mettre_nom_du_fichier_html.html", data = animaux_data)   #mettre le fichier html

@app.route('/createAnimaux', methods=['POST'])
def createAnimaux():
#id = request.form['id']
    famille_id = request.form['famille_id']
    sexe = request.form['sexe']
    presence = request.form['presence']
    apprivoise = request.form['apprivoise']
    mort_ne = request.form['mort_ne']
    decede= request.form['decede']
    if famille_id and decede:
        animauxController.insertUser(famille_id,sexe, presence, apprivoise, mort_ne, decede)
    return make_response(f"crée avec succès!")


