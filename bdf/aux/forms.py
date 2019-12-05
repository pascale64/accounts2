from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from bdf.models import User, Auxilliere


class AddAuxilliereForm(FlaskForm):
    id = StringField('auxilliere', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')

