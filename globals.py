import os
import googlemaps
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

STATIC_URI = os.path.join(os.getcwd(),"static")
TEMPLATES_URI = os.path.join(os.getcwd(),"templates")
DB_NAME = "database.db"
UPLOAD_FOLDER = "static/images"
SECRET_KEY = os.getenv("SECRET_KEY",None)

if SECRET_KEY == None:
    print("Secret key is required in .env")
    os._exit(0)


maps_apikey = os.getenv("GOOGLE_MAPS_APIKEY",None)
if maps_apikey == None:
    print("Missing google maps api key in .env")
    os._exit(0)

gmaps = googlemaps.Client(key=maps_apikey)

db = SQLAlchemy()
ma = Marshmallow()
