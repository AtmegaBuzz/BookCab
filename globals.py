import os
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DB_NAME = "database.db"
UPLOAD_FOLDER = "static/images"
SECRET_KEY = os.getenv("SECRET_KEY",None)

if SECRET_KEY == None:
    print("Secret key is required in .env")
    os._exit(0)

db = SQLAlchemy()
ma = Marshmallow()
