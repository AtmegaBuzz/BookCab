from flask import session, redirect, url_for
from functools import wraps

def is_authenticated(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["user"] == None:
            return redirect(url_for("auth.login"))
        
        return func(*args,**kwargs)

    return wrapper