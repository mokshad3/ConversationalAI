# app.py
from flask import Flask
from app_routes import index

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
file_handler.setLevel(logging.INFO)

logging.getLogger().addHandler(file_handler)


app = Flask(__name__)

@app.route('/route')
def main():
    app.logger.debug('This is a debug message')
    app.logger.info('This is an info message')
    app.logger.warning('This is a warning message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    return index()

if __name__ == "__main__":
    app.run()
