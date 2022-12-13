from globals import db 
from sqlalchemy.sql import func

class CabGroup(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    bookings = db.relationship('Booking',backref="cabgroup_bookings")

    

# root destination of the organization offering the services
class Source(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    location_name = db.Column(db.String(1000),nullable=False)



class Booking(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    destination = db.Column(db.String(50),nullable=True)
    status = db.Column(db.Integer,nullable=True) # 0 = booking ongoing | 1 = payment pending | 2 = booking accepted
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    cost = db.Column(db.Integer,nullable=True)
    distance = db.Column(db.Integer,nullable=True)
    booking_hash = db.Column(db.String(500),nullable=False)

    group = db.Column(db.Integer,db.ForeignKey('cab_group.id'))
    user = db.Column(db.Integer,db.ForeignKey('user.id'))
    def __str__(self):
        return f"{self.user} {self.destination} {self.status} {self.user.id}"


class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    phone_number = db.Column(db.String(16),nullable=True)
    password = db.Column(db.String(16),nullable=False)
    bookings = db.relationship('Booking',backref="user_bookings")

    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    update_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

