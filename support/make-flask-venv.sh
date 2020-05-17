#!/bin/bash


if [ $(which virtualenv) ]; then
	virtualenv --python=python3 venv

	if [ -d venv ]; then
		source venv/bin/activate
		pip install Flask
		pip install Flask-Script

		pip install Flask-HTTPAuth

		pip install Flask-Cors
		pip install Flask-RESTful

		pip install Flask-SocketIO
		pip install eventlet
		pip install requests

		pip freeze > "requirements.txt"
		deactivate
	fi
fi
