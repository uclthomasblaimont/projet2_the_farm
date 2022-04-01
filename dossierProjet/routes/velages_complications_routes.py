from flask import Blueprint
from flask import render_template, request, make_response
from controllers import velagescomplicationsController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
velagecomplication_bp = Blueprint('velagecomplication_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pageVelagecomplication', methods=['GET'])
def pageVelagecomplication():
    velagecomplication_data=velagescomplicationsController.getVelagecomplication()
    for velagecomplication in velagecomplication_data:
        print(velagecomplication.velage_id, velagecomplication.complication_id)
    return render_template("mettre_nom_du_fichier_html.html", data = velagecomplication_data)   #mettre le fichier html

@app.route('/createVelagecomplication', methods=['POST'])
def createVelagecomplication():
#id = request.form['id']
    velage_id = request.form['velage_id']
    complication_id = request.form['compication_id']
    if velage_id and complication_id:
        velagescomplicationsController.insertVelagecomplication(velage_id, complication_id)
    return make_response(f"succès!")

    