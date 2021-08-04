from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistroForm(FlaskForm):
    estado = StringField("Estado", validators=[DataRequired()])
    municipio = StringField("Municipio", validators=[DataRequired()])
    colonia = StringField("Colonia", validators=[DataRequired()])
    cp = StringField("Codigo Postal", validators=[DataRequired()])
    idasent = StringField("Identificador SEPOMEX")
    enviar = SubmitField("Enviar")
