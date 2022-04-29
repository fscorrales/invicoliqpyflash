from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flaskwebgui import FlaskUI
import sys
import os

#from database import db
#If using test enviroment
#TEST_ENV = False

""" if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder = template_folder, 
                static_folder = static_folder)
else:
    app = Flask(__name__) """

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# if TEST_ENV == False:
#   ui = FlaskUI(app)

DATABASE = 'slave_test.sqlite'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='llave_secreta'
#Inicializacion del objeto db de sqlalchemy
db = SQLAlchemy(app)
#db.init_app(app)

#configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

from invicoliqpy import routes
from invicoliqpy import fake_db