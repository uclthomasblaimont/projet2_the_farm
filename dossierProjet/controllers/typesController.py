import sys
from flask import render_template, redirect, url_for, request
from models.types import Types
from app import db


def getTypes():
    types_data = Types.query.all()
    for types in types_data:
        print(types.animal_id, types.type)
    return types_data

def insertTypes(animal_id, type):
    new_types = Types(animal_id=animal_id, type=type) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_types)
    db.session.commit()