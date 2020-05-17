def create_app(config_name):
	from flask import Flask
	app = Flask(__name__)

	from flask_cors import CORS
	CORS(app)

	from config import config
	app.config.from_object(config[config_name])

	from .extensions import socketio
	socketio.init_app(app)

	#from .extensions import background_task
	#socketio.start_background_task(background_task)

	from .main import main_blueprint
	app.register_blueprint(main_blueprint, url_prefix='/main')

	@app.before_request
	def before_request():
		pass

	@app.after_request
	def after_request(response):
		return response

	return app
