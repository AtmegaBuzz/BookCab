
import os
from flask import Flask
from globals import (
    UPLOAD_FOLDER,
    DB_NAME,
    SECRET_KEY,
    db,
    STATIC_URI,
    TEMPLATES_URI
)

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.static_folder = STATIC_URI
    app.template_folder = TEMPLATES_URI

    db.init_app(app)

    from backend.auth import auth 
    from backend.views import views

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth/')


    from backend.models import (
        User,
        Booking,
        CabGroup,
        Source
    )

    create_database(app)

    return app

def create_database(app):

    if not os.path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print("database created...")