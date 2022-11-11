from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    flash
)
from backend.forms import RegisterForm

auth = Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():

    user = session.get("user",None)
    form = RegisterForm()

    if user!=None:
        return redirect("/home")

    if request.method == "POST":

        if form.validate_on_submit():
            print(form.data)
        else:
            print(form.errors)        

        
    return render_template(
        'register.html',
        user = user,
        form=form
    )

@auth.route('/login',methods=['POST','GET'])
def login():

    user = session.get("user",None)
    if user!=None:
        return redirect("/home")

    if request.method == "POST":
        
        print(request.form)


        
    return render_template(
        'login.html',
        user = user
    ) 