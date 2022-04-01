from flask_sqlalchemy import SQLAlchemy
from app import db
class Complications(db.Model):     
    __tablename__= 'complications'    
    id = db.Column(db.Integer, primary_key=True) 
    complication = db.Column(db.String(120), nullable=False)  
      
    
    def __init__(self, animal_id,complication):
        self.animal_id= animal_id
        self.complication=complication
        