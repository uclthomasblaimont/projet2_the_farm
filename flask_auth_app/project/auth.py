from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/produit')
def produit():
    return render_template('produit.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # si cela renvoie un utilisateur, alors l'e-mail existe déjà dans la base de données

    if user: # si un utilisateur est trouvé, nous souhaitons le rediriger vers la page d'inscription afin que l'utilisateur puisse réessayer
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # créer un nouvel utilisateur avec les données du formulaire. Hachez le mot de passe pour que la version en clair ne soit pas enregistrée.

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # ajouter le nouvel utilisateur à la base de données
    db.session.add(new_user)
    db.session.commit()
 
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # vérifier si l'utilisateur existe réellement
    # prendre le mot de passe fourni par l'utilisateur, le hacher et le comparer au mot de passe haché dans la base de données
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # si l'utilisateur n'existe pas ou si le mot de passe est erroné, rechargez la page

    # le code de connexion va ici
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))



