from backend import create_app
from flask_socketio import SocketIO
# from flask_socketio import SocketIO, join_room, leave_room, send
# from flask import session


app = create_app()

socketio = SocketIO(app,cors_allowed_origins="*")

from backend.handlers import on_join_room,on_leave,handel_message


if __name__ == '__main__':
    app.debug = True
    socketio.run(app,debug=True)