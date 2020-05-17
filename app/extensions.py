from flask_socketio import SocketIO
socketio = SocketIO(cors_allowed_origins='*')


@socketio.on('connect')
def connect():
	pass


@socketio.on('disconnect')
def disconnect():
	pass
