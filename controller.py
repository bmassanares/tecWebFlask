# controllers.py

from flask import render_template

from aplicacao import app


def index():

return render_template(‘index.html’)