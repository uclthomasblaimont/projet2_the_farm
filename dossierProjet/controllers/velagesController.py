import sys
from flask import render_template, redirect, url_for, request
from models.velages import Velages
from app import db


def getVelages():
    velage_data = Velages.query.all()
    for velages in velage_data:
        print(velages.id, velages.mere_id, velages=pere_id, velages=date)
    return velage_data

def insertVelages(id, mere_id, pere_id, date):
    new_velage = Velages(id=id, mere_id=mere_id, pere_id=pere_id, date=date) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_velage)
    db.session.commit()

    
   