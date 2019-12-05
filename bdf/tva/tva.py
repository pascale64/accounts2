from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from bdf import db
from bdf.models import User, Book
from bdf.tva import bp
import time



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/tva', methods=['GET', 'POST'])
@login_required
def tva():
    book = Book.query.all()
    return render_template('tva/tva.html', books=books)
    

