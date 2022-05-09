from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models import User
    @login_manager.user_loader

    def load_user(user_id):
        # puisque le user_id n'est que la clé primaire de notre table d'utilisateurs, utilisez-le dans la requête pour l'utilisateur
        return User.query.get(int(user_id))
        
    
    # blueprint pour auth routes dans notre app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    # blueprint pour non partie de auth de app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
