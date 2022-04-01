from flask_sqlalchemy import SQLAlchemy
from app import db
class Familles(db.Model):     
    __tablename__= 'familles'    
    id = db.Column(db.Integer, primary_key=True) 
    nom = db.Column(db.String(120), nullable=False)  
       
    
    def __init__(self, id,nom):
        self.id= id
        self.nom=nom
        