
from flask import Blueprint, render_template, request


from . import db
from flask_login import login_required, current_user
from fonction import get_familles, get_date


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/acceuil')
@login_required
def profile():
    return render_template('acceuil.html', name=current_user.name)
@main.route('/formulaire', methods=['get', 'post'])
def formulaire():
    if request.method == 'POST':
        famille= request.form["choix_famille"]
        date_debut = request.form['debut']
        date_end = request.form['end']
        print("choix_famille:", famille, "start:", date_debut, "end:", date_end)
        return render_template("homeaffichage.html", **locals())
    else:
        return render_template("formulaire.html", familles = get_familles(), date=get_date())
