#adapted from https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example

from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)
thread = None
thread_lock = Lock() #we'll use this lock to prevent multiple clients from modifying thread at the same time


@app.route('/')
def index():
   
    return render_template('home.html', async_mode=socketio.async_mode)



@socket.on('connect')
def test_connet():
    #global thread # using the thread var created above. 
    #with thread_lock: # lock the thread so other clients can't change it.
        #if thread is None:
            #thread=sockio.start_background_task(target=background_through)
    emit('start''connected',)#name of event. send message to client



if __name__ == '__main__':
    socketio.run(app, debug=True)
