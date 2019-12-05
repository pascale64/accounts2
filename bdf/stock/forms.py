from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, FloatField, IntegerField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from wtforms.fields.html5 import DateField
from bdf.models import User, Stock
from flask_wtf.file import FileField, FileAllowed, FileRequired
from bdf import images

class AddStockForm(FlaskForm):
    id = StringField('sku', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(images, 'Images Only!')])
    date = DateField('date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    event = StringField('Event', validators=[DataRequired()])
    achat = FloatField('Prix de Achat', validators=[DataRequired()])
    vente = FloatField('Prix de Vente')
    QT = IntegerField('Quantity')
    sold = IntegerField('sold')
    submit = SubmitField('submit')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')
