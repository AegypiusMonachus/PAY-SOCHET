from app import create_app
app = create_app('DEBUGGING')


if __name__ == '__main__':
	from app.extensions import socketio
	socketio.run(app, port=8125)
