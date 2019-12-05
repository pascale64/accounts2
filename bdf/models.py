from bdf import db, login
from datetime import datetime
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from sqlalchemy import Integer, ForeignKey, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '{}'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(String(255))
    debit = db.Column(db.Integer, db.ForeignKey("general.id"))
    credit = db.Column(db.Integer, db.ForeignKey("general.id"))
    montant = db.Column(db.Float)
    AUX = db.Column(db.String(6), db.ForeignKey("auxilliere.id"))
    type = db.Column(db.String(6), db.ForeignKey("type.id"))
    REF = db.Column(db.String(6))
    JN = db.Column(db.String(6), db.ForeignKey("journal.id"))
    PID = db.Column(db.Integer, db.ForeignKey("period_id.id"))
    CT = db.Column(db.Float)
    
    deb = db.relationship("General", foreign_keys=[debit])
    cred = db.relationship("General", foreign_keys=[credit])
    auxil = db.relationship("Auxilliere")
    Types = db.relationship("Type")
    Journ = db.relationship("Journal")
    P_id = db.relationship("Period_id")
    
    def __repr__(self):
        return '{}'.format(self.id)
        
class General(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    
    def __repr__(self):
        return '{}'.format(self.id)
        

class Auxilliere(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(255))
    
    def __repr__(self):
        return '{}'.format(self.id)
        

class Type(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(255))
    
    def __repr__(self):
        return '{}'.format(self.id)
        

class Period_id(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    
    def __repr__(self):
        return '{}'.format(self.id)
        
class Journal(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(255))
    
    def __repr__(self):
        return '{}'.format(self.id)
        
class Stock(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    image_filename = db.Column(db.String(255), default=None, nullable=True)
    image_url = db.Column(db.String(255), default=None, nullable=True)
    date = db.Column(db.Date)
    description = db.Column(String(255))
    event = db.Column(String(255))
    achat = db.Column(db.Float)
    vente = db.Column(db.Float)
    QT = db.Column(db.Integer)
    sold = db.Column(db.Boolean)
    
    def __repr__(self):
        return '{}'.format(self.id)
        
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trans = db.Column(db.Integer)
    buyer = db.Column(db.String(255), db.ForeignKey("clients.name"))
    pays = db.Column(db.String(255))
    QT = db.Column(db.Integer)
    prix_de_vente = db.Column(db.Float)
    poste = db.Column(db.Float)
    total = db.Column(db.Float)
    paypal = db.Column(db.Integer)
    bordeaux = db.Column(db.Integer, db.ForeignKey("bordeauxbrocante.id"))
    frou = db.Column(db.Integer, db.ForeignKey("froufrou.id"))
    amazon = db.Column(db.String(255), db.ForeignKey("amazon.id"))
    products = db.Column(db.String(20), db.ForeignKey("stock.id"))
    PID = db.Column(db.Integer, db.ForeignKey("period_id.id"))
    date = db.Column(db.Date)
    description = db.Column(String(255))
    
    P_id = db.relationship("Period_id")
    client = db.relationship("Clients")
    marchandise = db.relationship("Stock")
    BB = db.relationship("Bordeauxbrocante")
    FF = db.relationship("Froufrou")
    AM = db.relationship("Amazon")
    
    def __repr__(self):
        return '{}'.format(self.id)
    

class Clients(db.Model):
    name = db.Column(db.String(255), primary_key=True)
    Add_1 = db.Column(db.String(255))
    Add_2 = db.Column(db.String(255))
    Ville = db.Column(db.String(255))
    Region = db.Column(db.String(255))
    CodePostale = db.Column(db.String(20))
    Pays = db.Column(db.String(255))
    
    
    def __repr__(self):
        return '{}'.format(self.name)
    
class Bordeauxbrocante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    buyer = db.Column(db.String(255), db.ForeignKey("clients.name"))
    avantcomm = db.Column(db.Float)
    comm = db.Column(db.Float)
    net = db.Column(db.Float)
    rate = db.Column(db.Float)
    REM = db.Column(db.Float)
    RemComm = db.Column(db.Float)

    
    client = db.relationship("Clients")
    
    def __repr__(self):
        return '{}'.format(self.id)

class Froufrou(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    buyer = db.Column(db.String(255), db.ForeignKey("clients.name"))
    avantcomm = db.Column(db.Float)
    comm = db.Column(db.Float)
    net = db.Column(db.Float)
    rate = db.Column(db.Float)
    REM = db.Column(db.Float)
    RemComm = db.Column(db.Float)

    
    client = db.relationship("Clients")
    
    def __repr__(self):
        return '{}'.format(self.id)
        
class Amazon(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    date = db.Column(db.Date)
    buyer = db.Column(db.String(255), db.ForeignKey("clients.name"))
    avantcomm = db.Column(db.Float)
    comm = db.Column(db.Float)
    net = db.Column(db.Float)
    rate = db.Column(db.Float)
    
    client = db.relationship("Clients")
    
    def __repr__(self):
        return '{}'.format(self.id)

class PayPal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    buyer = db.Column(db.String(255), db.ForeignKey("clients.name"))
    avantcomm = db.Column(db.Float)
    comm = db.Column(db.Float)
    net = db.Column(db.Float)
    rate = db.Column(db.Float)
    Cur = db.Column(db.String(3))
    REM = db.Column(db.Float)
    RemComm = db.Column(db.Float)
    
    client = db.relationship("Clients")
    
    def __repr__(self):
        return '{}'.format(self.id)
