from flask_socketio import join_room, leave_room, send
from flask import session

try:
    from __main__ import socketio
except ImportError:
    from server import socketio

@socketio.on('join')
def on_join_room(data):

    username = data['username']
    room = data['room']
    join_room(room)
    send({"user":session["user"],"message":"has enterd the chat"}, to=room,broadcast=True)

@socketio.on('leave')
def on_leave(data):

    username = data['username']
    room = data['room']
    leave_room(room)
    send({"user":session["user"],"message":"has left the chat"}, to=room,broadcast=True)


@socketio.on('message')
def handel_message(json):
    
    
    room = json["room"]
    message = json["message"]

    if message != "User Connected":
        send({"user":session["user"],"message":message},room=room,broadcast=True)



