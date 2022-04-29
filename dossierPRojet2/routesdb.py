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
