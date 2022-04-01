from flask import Blueprint
from flask import render_template, request, make_response
from controllers import velagesController
#importer app pour pouvoir utiliser @app.route
from app import app

#créer un objet blueprint pour le modèle animaux. 
velage_bp = Blueprint('velage_bp', __name__)
@app.route('/')
def index():
    return render_template('index.html')         #remplacer index par le fcihierhtml

@app.route('/pageVelages', methods=['GET'])
def pageVelages():
    velage_data=velagesController.getVelages()
    for velages in velage_data:
        print(velages.id, velages.mere_id, velages=pere_id, velages=date)
    return render_template("mettre_nom_du_fichier_html.html", data = velage_data)   #mettre le fichier html

@app.route('/createVelages', methods=['POST'])
def createVelages():
#id = request.form['id']
    id = request.form['id']
    mere_id = request.form['mere_id']
    pere_id= request.form['pere_id']
    date=request.form['date']
    if id and date:
        velagesController.insertVelages(id, mere_id, pere_id, date)
    return make_response(f"succès!")

    