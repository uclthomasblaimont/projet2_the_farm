import sys
from flask import render_template, redirect, url_for, request
from models.animaux import Animaux
from app import db


def getAnimaux():
    animaux_data = Animaux.query.all()
    for animaux in animaux_data:
        print(animaux.famille_id, animaux.sexe, animaux.presence, animaux.apprivoise, animaux.mort_ne, animaux.decede)
    return animaux_data

def insertUser(famille_id, sexe,  presence, apprivoise,mort_ne, decede):
    new_animals = Animaux(famille_id=famille_id,sexe=sexe, presence=presence, apprivoise=apprivoise, mort_ne=mort_ne, decede=decede) #instanciation d'un objet de type User
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_animals) 
    db.session.commit() 