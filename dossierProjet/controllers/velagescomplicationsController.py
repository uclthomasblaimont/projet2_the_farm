import sys
from flask import render_template, redirect, url_for, request
from models.velages_complications import VelagesComplication
from app import db


def getVelagecomplication():
    velagecomplication_data = VelagesComplication.query.all()
    for velagecomplication in velagecomplication_data:
        print(velagecomplication.velage_id, velagecomplication.complication_id)
    return velagecomplication_data

def insertVelagecomplication(velage_id, complication_id):
    new_velagescomplication = VelagesComplication(velage_id=velage_id, complication_id=complication_id) 
#L'objet Session de SQLAlchemy gère toutes les opérations de persistance pour les objets ORM.
    db.session.add(new_velagescomplication)
    db.session.commit()

