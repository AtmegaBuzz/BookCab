import random
from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from backend.decorators import is_authenticated
from backend.forms import BookCabForm
from globals import maps_apikey
from backend.models import Booking, User, CabGroup
from backend.algorithm import main
from globals import db

views = Blueprint("views",__name__)

@views.route("/",methods=["GET","POST"])
@is_authenticated
def home():

    form = BookCabForm()

    if request.method == "POST":
        
        if form.validate_on_submit():
            destination = form.data["destination"]
        
            try:
                # booking having status code ongoing
                bookings_ongoing = Booking.query.filter_by(status=0).all()

                # create bookings if there are more than 4 ongoing request in queue
                user = User.query.filter_by(email=session["user"]).first()
                curr_booking = Booking(destination=destination,user=user.id,status=0)
                db.session.add(curr_booking)
                db.session.commit()

                if len(bookings_ongoing)>=3:
                    print(bookings_ongoing)
                    groups =  main()    
                    
                    for group in groups:
                        name = f"grp{random.randint(1,10000)}:{random.randbytes(10000)}"
                        grp = CabGroup(name=name)
                        db.session.add(CabGroup)
                        db.session.commit()

                        for usrAttr in group:
                        
                            booking_a = Booking.query.filter_by(id=usrAttr.booking_id).all()
                            for booking_ in booking_a:
                                
                                booking_.status = 1
                                booking_.group = grp.id
                                booking_.cost = usrAttr.cost
                                booking_.distance = usrAttr.distance

                            db.session.add_all(booking_a)
                            db.session.commit()

                            print("booking added")
                            flash("Booking added")
                        
                else:
                    flash("request added successfuly")
                    
                        
            except Exception as e:
                print(e,"=========")
                flash("allocation failed try again later!")
        
        else:
            flash(form.errors)

    return render_template(
        "index.html",
        user = session["user"],
        form = form,
        google_maps_apikey = maps_apikey
    )


@views.route("/services",methods=["GET"])
@is_authenticated
def services():

    user = User.query.filter_by(email=session["user"]).first()
    if user == None:
        return redirect(url_for("auth.login"))

    curr_bookings = Booking.query.filter_by(user=user.id).all()

    return render_template(
        "services.html",
        user = session["user"],
        bookings = curr_bookings
    )

@views.route("/contact",methods=["GET"])
@is_authenticated
def contact():

    user = User.query.filter_by(email=session["user"]).first()
    if user == None:
        return redirect(url_for("auth.login"))

    return render_template(
        "contact.html",
        user = session["user"],
    )
