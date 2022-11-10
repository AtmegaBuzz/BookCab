from flask import Blueprint, render_template, session, request


auth = Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():

    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST': 
        return render_template('register.html')
