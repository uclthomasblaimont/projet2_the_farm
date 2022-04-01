from flask_sqlalchemy import SQLAlchemy
from app import db
class AnimauxTypes(db.Model):     
    __tablename__= 'animauxtypes'    
    animal_id = db.Column(db.Integer, primary_key=True) 
    type_id = db.Column(db.Integer(), nullable=False)  
    pourcentage= db.Column(db.Integer(), nullable=False)   
    
    def __init__(self, animal_id,type_id, pourcentage):
        self.animal_id= animal_id
        self.type_id=type_id
        self.pourcentage = pourcentage
     