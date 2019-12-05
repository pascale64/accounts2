from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField,\
                      FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from bdf.models import User, Book, General, Auxilliere, Journal, Period_id, Type
from wtforms_alchemy.fields import QuerySelectField

def general_ID():
    return General.query

def aux_ID():
    return Auxilliere.query
    
def pid_ID():
    return Period_id.query
    
def type_ID():
    return Type.query
    
def jn_ID():
    return Journal.query

class AddBookForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    debit = IntegerField('Debit')
    credit = IntegerField('Credit')
    montant = FloatField('Montant', validators=[DataRequired()])
    AUX = StringField('Auxilliare')
    type = StringField('Type')
    REF = StringField('REF')
    JN = StringField('JN')
    PID = IntegerField('PID')
    CT = IntegerField('CT')
    submit = SubmitField('Submit')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')

class AddJnForm(FlaskForm):
    id = StringField('Journal', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')


class AddPidForm(FlaskForm):
    id = IntegerField('Period', validators=[DataRequired()])
    start = DateField('Start Date', validators=[DataRequired()])
    end = DateField('End Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')
    
class AddTypeForm(FlaskForm):
    id = StringField('Type', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')
