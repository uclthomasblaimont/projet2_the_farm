from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#associer le fichier de configuration
app.config.from_object('config')
db = SQLAlchemy(app)
#Importer le modèle User
from models.animaux import Animaux
from models.animaux_types import AnimauxTypes
from models.animaux_velages import AnimauxVelages
from models.complications import Complications
from models.familles import Familles
from models.types import Types
from models.velages import Velages
from models.velages_complications import VelagesComplication
#Créer le modèle
db.create_all()
if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
    app.run()
