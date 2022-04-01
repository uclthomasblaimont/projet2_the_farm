import sys
from flask import render_template, redirect, url_for, request
from models.animaux_types import AnimauxTypes
from app import db


def getAnimauxtypes():
    animauxtypes_data = AnimauxTypes.query.all()
    for animauxtypes in animauxtypes_data:
        print(animauxtypes.animal_id, animauxtypes.type_id, animauxtypes.pourcentage)
    return animauxtypes_data

def insertAnimauxtypes(animal_id, type_id,  pourcentage):
    new_animalstypes = AnimauxTypes(animal_id=animal_id,type_id=type_id, pourcentage=pourcentage) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_animalstypes)
    db.session.commit()
