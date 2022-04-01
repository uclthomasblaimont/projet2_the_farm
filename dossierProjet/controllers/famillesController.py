import sys
from flask import render_template, redirect, url_for, request
from models.familles import Familles
from app import db


def getFamilles():
    famille_data = Familles.query.all()
    for famille in famille_data:
        print(famille.id, famille.nom)
    return famille_data

def insertFamilles(id, nom):
    new_familles = Familles(id=id, nom=nom) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_familles)
    db.session.commit()