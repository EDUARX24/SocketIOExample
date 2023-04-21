from flask import Flask, render_template, url_for
from flask_socketio import emit, join_room, SocketIO

app = Flask(__name__)
Socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

#Add to rom
@SocketIO.on("join_room")
def entrar(room):

    join_room(room)

    emit('mensaje', f"Un usuario ha ingresado a la sala {room}", 
         broadcast = False, include_self=False, to=room)
    
    return room 

#send message
@Socketio.on("message")
def message(data):
    emit("message", data["message"], broadcast=False, include_self = True,
         to = data["room"])
