from flask_sqlalchemy import SQLAlchemy
from app import db
class AnimauxVelages(db.Model):     
    __tablename__= 'animauxvelages'    
    animal_id = db.Column(db.Integer, nullable=False, primary_key=True) 
    velage_id = db.Column(db.Integer(), nullable=False, primary_key=True)  
      
    
    def __init__(self, animal_id,velage_id):
        self.animal_id= animal_id
        self.velage_id=velage_id
        