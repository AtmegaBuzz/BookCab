from flask import session, redirect, url_for
from functools import wraps
from backend.models import User

def is_authenticated(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        user_obj = User.query.filter_by(email=session["user"]).first()
        if session["user"] == None or user_obj == None:
            return redirect(url_for("auth.login"))
        
        return func(*args,**kwargs)

    return wrapper