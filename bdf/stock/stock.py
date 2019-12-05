from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from io import TextIOWrapper
import csv
from flask_login import current_user, login_required
from bdf import db
from bdf import images
from bdf.models import User, Stock
from bdf.stock import bp
from bdf.stock.forms import AddStockForm
from werkzeug.utils import secure_filename
import time
from flask_paginate import Pagination, get_page_args
from werkzeug.urls import url_parse
from sqlalchemy import desc

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/stock', methods=['GET', 'POST'])
@login_required
def stock():
    stocks = Stock.query.order_by(desc(Stock.id))
    forms = []
    def get_forms(offset=0, per_page=25):
        return forms[offset: offset + per_page]
    for stock in stocks:
        form = AddStockForm()
        form.id.default = stock.id
        form.image.default = stock.image_url
        form.date.default = stock.date
        form.description.default = stock.description
        form.event.default = stock.event
        form.achat.default = stock.achat
        form.vente.default = stock.vente
        form.QT.default = stock.QT
        form.sold.default = stock.sold
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                stock = Stock.query.filter_by(id=form.id.data).one()
                stock.date = form.date.data
                stock.description = form.description.data
                stock.event = form.event.data
                stock.achat = form.achat.data
                stock.vente = form.vente.data
                stock.QT = form.QT.data
                stock.sold = form.sold.data
                db.session.add(stock)
                db.session.commit()
            elif form.delete.data:
                stock = Stock.query.filter_by(id=form.id.data).one()
                db.session.delete(stock)
                db.session.commit()
            return redirect(url_for('stock.stock'))

        page, per_page, offset = get_page_args(page_parameter='page',
                                  per_page_parameter='per_page')
        total = len(forms)
        pagination_forms = get_forms(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total)
        form.process()  # Do this after validate_on_submit or breaks CSRF token

    return render_template('stock/stock.html', title=Stock, stocks=stocks,
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)



@bp.route('/stock/add_stock', methods=('GET', 'POST'))
@bp.route('/stock/add_stock', methods=('GET', 'POST'))
@login_required
def add_stock():
    form = AddStockForm()
    if form.validate_on_submit():
        filename = images.save(request.files['image'])
        url = images.url(filename)
        obj = Stock(id=form.id.data, date=form.date.data, description=form.description.data,
              event=form.event.data, achat=form.achat.data, vente=form.vente.data, 
              sold=form.sold.data, image_filename=filename, image_url=url)
        db.session.add(obj)
        db.session.commit()
        flash('Congratulations, you have now a registered a new Aux!')
        return redirect(url_for('stock.stock'))
    return render_template('stock/add_stock.html', form=form)

@bp.route('/stock/_edit_stock', methods=('GET', 'POST'))
@bp.route('/stock/_edit_stock/<int:id>', methods=('GET', 'POST'))
@login_required
def _edit_stock(id):
    stock = Stock.query.all
    obj = Stock.query.get(id) or Stock()
    form = AddStockForm(request.form, obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        return redirect(url_for('stock.stock'))
    return render_template('stock/_edit_stock.html', form=form, stock=stock)


@bp.route('/stock/upload_stock', methods=['GET', 'POST'])
@login_required
def upload_stock():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            stock = Stock(id=row[0], image_filename=row[2], image_url=row[1],date=row[3],
                          description=row[4], event=row[5], achat=row[6], vente=row[7],
                          QT=row[8] )
            db.session.add(stock)
            db.session.commit()
        return redirect(url_for('stock.stock'))
    return render_template('stock/upload_stock.html')
    
@bp.route('/control/delete_stock/<int:id>', methods=['GET','POST'])
@login_required
def delete_stock(id):
    obj = Stock.query.get(id) or Stock()
    db.session.delete(obj)
    db.session.commit()
    flash('Congratulations, you have deleted an Item!')
    return redirect(url_for('stock.stock'))
