from flask import Blueprint
from flask import render_template, request, make_response
from controllers import animauxvelagesController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
animauxvelage_bp = Blueprint('animauxvelage_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pagevelageAnimaux', methods=['GET'])
def pagevelageAnimaux():
    animauxvelage_data=animauxvelagesController.getAnimauxVelage()
    for animauxvelage in animauxvelage_data:
        print(animauxvelage.animal_id, animauxvelage.velage_id)
    return render_template("mettre_nom_du_fichier_html.html", data = animauxvelage_data)   #mettre le fichier html

@app.route('/createAnimauxvelage', methods=['POST'])
def createAnimauxvelage():
#id = request.form['id']
    animal_id = request.form['famille_id']
    velage_id = request.form['velage_id']
    if animal_id and velage_id:
        animauxvelagesController.insertAnimauxVelage(animal_id, velage_id)
    return make_response(f"succès!")