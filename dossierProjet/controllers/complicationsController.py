import sys
from flask import render_template, redirect, url_for, request
from models.complications import Complications
from app import db


def getComplication():
    complication_data = Complications.query.all()
    for complication in complication_data:
        print(complication.animal_id, complication.velage_id)
    return complication_data

def insertComplication(animal_id, complication):
    new_complication = Complications(animal_id=animal_id,complication=complication) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_complication)
    db.session.commit()

