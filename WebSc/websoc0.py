import time
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def connected():
    socketio.send('Connected to http://127.0.0.1:5000')
    print('client connected')


@socketio.on('disconnect')
def disconnected():
    print('client disconnected')


@socketio.on('message')
def handle_message(message):
    # print('message: ' + message['data'])
    print(message)
    send('message sent me: ' + message)


@socketio.on('json')
def handle_json(json):
    print('json: ' + str(json))
    send('json sent me', broadcast=True)


@socketio.on('my_event')
def myCustomevents(json):
    print('my_event: ' + str(json))
    while True:
        time.sleep(3)
        send(str(json) + str(random.randint(0, 100)))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('my event: ' + str(json))
    send('my event sent me', broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
