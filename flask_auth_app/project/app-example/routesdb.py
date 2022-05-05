

import sqlite3
import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .db import get_annee, get_familles, get_mois
bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/accueil/formulaire', methods = ["get", "post"])
def formulaire():
    """
    #retourne le contenu de la page index.html
    """
    if request.method == 'POST':
        choix_famille= request.form['choix_famille']
        choix_annee = request.form['choix_annee']
        choix_mois = request.form['choix_mois']
        print("choix_famille:", choix_famille, "choix_annee:", choix_annee, "choix_mois:", choix_mois)
        return render_template("homeaffichage.html", **locals())
    else:
        return render_template("formulaire.html", familles=get_familles(), mois=get_mois(), annee=get_annee())


@bp.route('home.home', methods=["get","post"])
def home():
    return render_template('index.html', familles= get_familles())
@bp.route('/home.affichage', methods=['get','post'])
def affichage():
    choix_famille= request.form['choix_famille']
    choix_annee = request.form['choix_annee']
    choix_mois = request.form['choix_mois']
    print("choix_famille", choix_famille, "choix_annee", choix_annee, "choix_mois", choix_mois)
    return render_template("homeaffichage.html", **locals())



#####################################################################



""" def atester():
    database = sqlite3.connect('test.db')
    cursor = database.cursor()
    if request.method == 'POST':
        famille = request.form["famille"]
        mois = request.form['mois']
        annee= request.form['annee']
        graph = request.method['graph']
        if graph == 'Nombre de velages':
            famille_choisis = ""
            if annee == 'Choisissez une année':
                return render_template("index.html", familles = famille,mois=mois, annee = annee , graph = graph)
            else:
                if famille == "Choix famille":
                    cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/%%/{}'".format(annee))
                else:
                    cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/%%/{} AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom LIKE '{}')))".format(annee, famille))
    velages = cursor.fetchall()
    dates =[]
    amount = []
    for v in velages:
        if get_familles() == "Choix famille":
            if v["date"] not in dates:
                cursor.execute("SELECT date FROM velages WHERE date LIKE '{}'".format(v["date"]))
                dates.append(v["date"])
                amount.append(len(cursor.fetchall()))
        else:
            if v["date"] not in dates:
                cursor.execute("SELECT date FROM velages WHERE date LIKE '{}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom LIKE '{}')))".format(v['date'], famille))
                dates.append(v['date'])
                amount.append(len(cursor.fetchall()))
    return render_template("index.html", results=[len(velages), annee, famille_choisis], labels = dates, amount = amount) """