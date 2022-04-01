from flask_sqlalchemy import SQLAlchemy
from app import db
class Types(db.Model):     
    __tablename__= 'types'    
    animal_id = db.Column(db.Integer, primary_key=True) 
    type= db.Column(db.String(120), nullable=False)  
   
    
    def __init__(self, animal_id,type):
        self.animal_id= animal_id
        self.type=type
    