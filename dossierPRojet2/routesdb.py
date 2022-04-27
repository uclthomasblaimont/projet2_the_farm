import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .db import get_familles
bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template("index.html", familles=get_familles())