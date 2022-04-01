from flask import Blueprint
from flask import render_template, request, make_response
from controllers import animauxtypesControllers
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
animauxtypes_bp = Blueprint('animauxtypes_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagetypeAnimaux', methods=['GET'])
def pagetypeAnimaux():
    animauxtype_data=animauxtypesControllers.getAnimauxtypes()
    for animauxtypes in animauxtype_data:
        print(animauxtypes.animal_id, animauxtypes.type_id, animauxtypes.pourcentage)
    return render_template("mettre_nom_du_fichier_html.html", data = animauxtype_data)   #mettre le fichier html

@app.route('/createAnimauxtype', methods=['POST'])
def createAnimauxtype():
#id = request.form['id']
    animal_id = request.form['famille_id']
    type_id = request.form['sexe']
    pourcentage = request.form['presence']
    if animal_id and pourcentage:
        animauxtypesControllers.insertAnimauxtypes(animal_id, type_id, pourcentage)
    return make_response(f"succès!")
