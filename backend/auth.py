from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    flash,
    url_for
)
from backend.forms import RegisterForm,LoginForm
from backend.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from globals import db

auth = Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():

    user = session.get("user",None)
    form = RegisterForm()

    if user!=None:
        return redirect(url_for("views.home"))

    if request.method == "POST":

        if form.validate_on_submit():
            if User.query.filter_by(email=form.data["email"]).first() == None:


                new_user = User(
                    name = form.data["name"],
                    email = form.data["email"],
                    phone_number = form.data["phone_number"],
                    password = generate_password_hash(form.data["password"],'sha256')
                )
                
                db.session.add(new_user)
                db.session.commit()

                flash("User created successfully")
                return redirect(url_for("auth.login"))

            flash("Email already exists")

        else:
            flash(form.errors)       

        
    return render_template(
        'register.html',
        user = user,
        form = form
    )

@auth.route('/login',methods=['POST','GET'])
def login():

    user = session.get("user",None)
    if user!=None:
        return redirect(url_for("views.home"))
    
    form = LoginForm()

    if request.method == "POST":
        
        if form.validate_on_submit():

            user = User.query.filter_by(
                email = form.data["email"]
            ).first()

            if user and check_password_hash(user.password,form.data["password"]):
                session["user"] = user.email
                return redirect(url_for("views.home"))

            flash("Incorrect Credentials")

        else:
            flash(form.errors)


        
    return render_template(
        'login.html',
        user = user,
        form = form
    ) 
