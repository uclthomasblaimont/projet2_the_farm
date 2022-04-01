
import sys
from flask import render_template, redirect, url_for, request
from models.animaux_velages import AnimauxVelages
from app import db


def getAnimauxVelage():
    animauxvelage_data = AnimauxVelages.query.all()
    for animauxvelage in animauxvelage_data:
        print(animauxvelage.animal_id, animauxvelage.velage_id)
    return animauxvelage_data

def insertAnimauxVelage(animal_id, velage_id):
    new_animalsvelages = AnimauxVelages(animal_id=animal_id,velage_id=velage_id) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_animalsvelages)
    db.session.commit()