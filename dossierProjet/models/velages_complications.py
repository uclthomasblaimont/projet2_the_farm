from flask_sqlalchemy import SQLAlchemy
from app import db
class VelagesComplication(db.Model):     
    __tablename__= 'velagescomplication'    
    velage_id = db.Column(db.Integer, primary_key=True) 
    complication_id = db.Column(db.Integer(), nullable=False, primary_key=True)  
 
    
    def __init__(self, velage_id,complication_id):
        self.velage_id= velage_id
        self.complication_id=complication_id
