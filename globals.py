import googlemaps
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

STATIC_URI = os.path.join(os.getcwd(),"static")
TEMPLATES_URI = os.path.join(os.getcwd(),"templates")
DB_NAME = "database.db"
UPLOAD_FOLDER = "static/images"
SECRET_KEY = os.getenv("SECRET_KEY",None)
SOURCE = os.getenv("ORG_SOURCE",None)
maps_apikey = os.getenv("GOOGLE_MAPS_APIKEY",None)

if SOURCE == None:
    print("ORG_SOURCE is required in .env")

if SECRET_KEY == None:
    print("Secret key is required in .env")
    os._exit(0)


if maps_apikey == None:
    print("Missing google maps api key in .env")
    os._exit(0)

gmaps = googlemaps.Client(key=maps_apikey)

db = SQLAlchemy()
