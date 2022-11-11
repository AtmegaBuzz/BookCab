from flask import Blueprint, render_template, session
from backend.decorators import is_authenticated

views = Blueprint("views",__name__)

@views.route("/",methods=["GET"])
@is_authenticated
def home():

    print(session["user"])
    
    return render_template(
        "index.html",
        user = session["user"]
    )