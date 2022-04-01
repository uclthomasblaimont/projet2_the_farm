from datetime import date
from flask_sqlalchemy import SQLAlchemy
from app import db
class Velages(db.Model):     
    __tablename__= 'velages'    
    id = db.Column(db.Integer, primary_key=True) 
    mere_id = db.Column(db.Integer(), nullable=False)  
    pere_id= db.Column(db.Integer(), nullable=False)   
    date= db.Column(db.Date, nullable=False)
    def __init__(self, id,mere_id, pere_id, date):
        self.id= id
        self.mere_id=mere_id
        self.pere_id = pere_id
        self.date=date