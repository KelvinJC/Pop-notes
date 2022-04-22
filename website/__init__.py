from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import settings

db = SQLAlchemy()
DB_NAME = settings.database_name


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = settings.secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .models import User, Note
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)
    
    # how flask should load a user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # check on path to verify that database has not been created
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
