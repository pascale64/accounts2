from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_paginate import Pagination, get_page_args
from io import TextIOWrapper
import csv
from bdf.books.forms import AddBookForm, AddJnForm, AddPidForm, AddTypeForm
from flask_login import current_user, login_required
from bdf import db
from bdf.models import User, Book, Journal, Period_id, Type
from bdf.books import bp
import time



@bp.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    books = Book.query.order_by(Book.date.desc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for book in books:
        form = AddBookForm()
        form.id.default = book.id
        form.date.default = book.date
        form.description.default = book.description
        form.debit.default = book.debit
        form.credit.default = book.credit
        form.montant.default = book.montant
        form.AUX.default = book.AUX
        form.type.default = book.type
        form.REF.default = book.REF
        form.JN.default = book.JN
        form.PID.default = book.PID
        form.CT.default = book.CT
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                book = Book.query.filter_by(id=form.id.data).one()
                book.date = form.date.data
                book.description = form.description.data
                book.debit = form.debit.data
                book.credit = form.credit.data
                book.montant = form.montant.data
                book.AUX = form.AUX.data
                book.type = form.type.data
                book.REF = form.REF.data
                book.JN = form.JN.data
                book.PID = form.PID.data
                book.CT = form.CT.data
                db.session.add(book)
                db.session.commit()
            elif form.delete.data:
                book = Book.query.filter_by(id=form.id.data).one()
                db.session.delete(book)
                db.session.commit()
            return redirect(url_for('books.books'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('books/books.html', books=books, title='Books',
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)




@bp.route('/books/upload_book', methods=['GET', 'POST'])
@login_required
def upload_book():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='ISO-8859-1')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            book = Book(id=row[0], date=row[1], description=row[2], debit=row[3], credit=row[4],\
                            montant=row[5], AUX=row[6], type=row[7], REF=row[8], JN=row[9], PID=row[10], CT=row[11])
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('books.books'))
    return render_template('books/upload_book.html')

@bp.route('/books/add_book', methods=('GET', 'POST'))
@login_required
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        obj = Book(id=form.id.data, date=form.date.data, description=form.description.data, debit=form.debit.data,\
                  credit=form.credit.data, montant=form.montant.data, AUX=form.AUX.data, type=form.type.data,\
                  REF=form.REF.data, JN=form.JN.data, PID=form.PID.data, CT=form.CT.data)
        db.session.add(obj)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Aux!')
        return redirect(url_for('books.books'))
    return render_template('books.add_book.html', form=form)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/books/jn', methods=['GET', 'POST'])
@login_required
def jn():
    jns = Journal.query.order_by(Journal.id.asc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for jn in jns:
        form = AddJnForm()
        form.id.default = jn.id
        form.name.default = jn.name
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                jn = Journal.query.filter_by(id=form.id.data).one()
                jn.name = form.name.data
                db.session.add(jn)
                db.session.commit()
            elif form.delete.data:
                jn = Journal.query.filter_by(id=form.id.data).one()
                db.session.delete(jn)
                db.session.commit()
            return redirect(url_for('books.jn'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('books/jn.html', jns=jns, title='Jounal',
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/books/pid', methods=['GET', 'POST'])
@login_required
def pid():
    pids = Period_id.query.order_by(Period_id.id.asc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for pid in pids:
        form = AddPidForm()
        form.id.default = pid.id
        form.start.default = pid.start
        form.end.default = pid.end
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                pid = Period_id.query.filter_by(id=form.id.data).one()
                pid.start = form.start.data
                pid.end = form.end.data
                db.session.add(pid)
                db.session.commit()
            elif form.delete.data:
                pid = Period_id.query.filter_by(id=form.id.data).one()
                db.session.delete(pid)
                db.session.commit()
            return redirect(url_for('books.pid'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('books/pid.html', pids=pids, title='Period_id',
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/books/type', methods=['GET', 'POST'])
@login_required
def type():
    types = Type.query.order_by(Type.id.asc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for type in types:
        form = AddTypeForm()
        form.id.default = type.id
        form.name.default = type.name
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                type = Type.query.filter_by(id=form.id.data).one()
                type.name = form.name.data
                db.session.add(type)
                db.session.commit()
            elif form.delete.data:
                type = Type.query.filter_by(id=form.id.data).one()
                db.session.delete(type)
                db.session.commit()
            return redirect(url_for('books.type'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('books/type.html', types=types, title='Types',
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)

@bp.route('/add_jn', methods=('GET', 'POST'))
@login_required
def add_jn():
    form = AddJnForm()
    if form.validate_on_submit():
        jn = Journal(id=form.id.data, name=form.name.data)
        db.session.add(jn)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Journal!')
        return redirect(url_for('books.jn'))
    return render_template('books/add_jn.html', form=form)


@bp.route('/add_pid', methods=('GET', 'POST'))
@login_required
def add_pid():
    form = AddPidForm()
    if form.validate_on_submit():
        pid = Period_id(id=form.id.data, start=form.start.data, end=form.end.data)
        db.session.add(pid)
        db.session.commit()
        flash('Congratulations, you have now a registered a new PID!')
        return redirect(url_for('books.pid'))
    return render_template('books/add_pid.html', form=form)


@bp.route('/add_type', methods=('GET', 'POST'))
@login_required
def add_type():
    form = AddTypeForm()
    if form.validate_on_submit():
        type = Type(id=form.id.data, name=form.name.data)
        db.session.add(type)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Type!')
        return redirect(url_for('books.type'))
    return render_template('books/add_type.html', form=form)

@bp.route('/books/upload_pid', methods=['GET', 'POST'])
@login_required
def upload_pid():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            pid = Period_id(id=row[0], name=row[1])
            db.session.add(pid)
            db.session.commit()
        return redirect(url_for('books.pid'))
    return render_template('books/upload_pid.html')
    
@bp.route('/books/upload_jn', methods=['GET', 'POST'])
@login_required
def upload_jn():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            jn = Journal(id=row[0], name=row[1])
            db.session.add(jn)
            db.session.commit()
        return redirect(url_for('books.jn'))
    return render_template('books/upload_jn.html')
    
@bp.route('/books/upload_type', methods=['GET', 'POST'])
@login_required
def upload_type():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ty = Type(id=row[0], name=row[1])
            db.session.add(ty)
            db.session.commit()
        return redirect(url_for('books.type'))
    return render_template('books/upload_type.html')
