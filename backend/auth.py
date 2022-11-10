from flask import Blueprint, render_template, session, request, redirect


auth = Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():

    user = session.get("user",None)
    if user!=None:
        return redirect("/home")

    if request.method == "POST":
        
        print(request.form)


        
    return render_template(
        'register.html',
        user = user
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