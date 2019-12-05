from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from bdf.models import User, General


class AddGeneralForm(FlaskForm):
    id = StringField('General')
    name = StringField('name')
    submit = SubmitField('Sign In')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')

