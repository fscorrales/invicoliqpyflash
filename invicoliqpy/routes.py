from flask import render_template, url_for
from werkzeug.utils import redirect
from invicoliqpy import app
from invicoliqpy.models import Factureros

#http://localhost:5000/
@app.route('/')
def inicio():
    #factureros = Factureros.query
    return render_template('prueba.html', total = 10)