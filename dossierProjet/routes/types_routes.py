from flask import Blueprint
from flask import render_template, request, make_response
from controllers import typesController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
type_bp = Blueprint('type_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pageType', methods=['GET'])
def pageType():
    type_data=typesController.getTypes()
    for types in types_data:
        print(types.animal_id, types.type)
    return render_template("mettre_nom_du_fichier_html.html", data = type_data)   #mettre le fichier html

@app.route('/createType', methods=['POST'])
def createType():
#id = request.form['id']
    animal_id = request.form['id']
    type = request.form['nom']
    if animal_id and type:
        typesController.insertTypes(animal_id, type)
    return make_response(f"succès!")