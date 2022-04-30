
import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .db import get_annee, get_familles, get_mois
bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template("index.html", familles=get_familles(), mois=get_mois(), annee=get_annee())
@bp.route('/home.affichage', methods=['get','post'])
def affichage():
    choix_famille=request.form['choix_famille']
    choix_annee = request.form['choix_annee']
    choix_mois = request.form['choix_mois']
    print("choix_famille", choix_famille, "choix_annee", choix_annee, "choix_mois", choix_mois)
    return 'page de traitement'