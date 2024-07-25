#!/bin/sh
# Defines the main script to be executed by Flask
export FLASK_APP=./cashman/index.py
# Runs our Flask app in the context of the virtual environment listening to all interfaces on the computer (-h 0.0.0.0)
pipenv run flask --debug run -h 0.0.0.0