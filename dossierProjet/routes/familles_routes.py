from flask import Blueprint
from flask import render_template, request, make_response
from controllers import famillesController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
famille_bp = Blueprint('famille_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pageFamille', methods=['GET'])
def pageFamille():
    famille_data=famillesController.getFamilles()
    for famille in famille_data:
        print(famille.id, famille.nom)
    return render_template("mettre_nom_du_fichier_html.html", data = famille_data)   #mettre le fichier html

@app.route('/createFamille', methods=['POST'])
def createFamilles():
#id = request.form['id']
    id = request.form['id']
    nom = request.form['nom']
    if id and nom:
        famillesController.insertFamilles(id, nom)
    return make_response(f"succès!")