from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FacturerosForm(FlaskForm):
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired()])
    actividad = StringField('Actividad', validators=[DataRequired()])
    partida = StringField('Partida', validators=[DataRequired()])
    enviar = SubmitField('Enviar')