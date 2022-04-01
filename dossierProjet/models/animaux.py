from flask_sqlalchemy import SQLAlchemy
from app import db
class Animaux(db.Model):      #cette classe av se charger pour faire exister le modèle. 
    __tablename__= 'animaux'    #nom de la table qui va êtré crée en base donnée et va être associer à ce modèle user. 
    id = db.Column(db.Integer, primary_key=True)  #on crée une colone appelé id et cetet colone la est du type integer et on indique qu'elle sera la clé primaire de cette table.  
    famille_id = db.Column(db.Integer())  
    sexe= db.Column(db.String(120))   #on défini la clé name et city par 120 caractère ce qui correspond dans le langage sql, taille max du texte qu'on pourra mettre dans le champ en question. 
    presence = db.Column(db.Integer(), nullable= False)
    apprivoise = db.Column(db.Integer(), nullable = False)
    mort_ne = db.Column(db.Integer(), nullable= False)
    decede = db.Column(db.Integer(), nullable = False)

    def __init__(self, famille_id,sexe, presence, apprivoise, mort_ne, decede):
        self.famille_id= famille_id
        self.sexe=sexe
        self.presence = presence
        self.apprivoise = apprivoise
        self.mort_ne= mort_ne
        self.decede= decede