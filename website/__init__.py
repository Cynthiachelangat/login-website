from flask import Flask
from website.config import Config
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
Db_name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{Db_name}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')

    from .models import User, Note

     # Ensure the database is created when the app starts
    with app.app_context():
        create_database()
    
    return app

def create_database():
    if not path.exists('website/' + Db_name):
        db.create_all()
        print('Created Database!')