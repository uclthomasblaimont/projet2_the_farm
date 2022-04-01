from flask import Blueprint
from flask import render_template, request, make_response
from controllers import complicationsController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
complication_bp = Blueprint('complication_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pageComplication', methods=['GET'])
def pageComplication():
    complication_data=complicationsController.getComplication()
    for complication in complication_data:
        print(complication.animal_id, complication.velage_id)
    return render_template("mettre_nom_du_fichier_html.html", data = complication_data)   #mettre le fichier html

@app.route('/createComplication', methods=['POST'])
def createComplication():
#id = request.form['id']
    animal_id = request.form['famille_id']
    complication = request.form['compliclation']
    if animal_id and velage_id:
        complicationsController.insertComplication(animal_id, complication)
    return make_response(f"succès!")