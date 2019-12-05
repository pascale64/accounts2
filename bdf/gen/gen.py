from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from io import TextIOWrapper
from flask_login import current_user, login_required
from bdf import db
from flask_paginate import Pagination, get_page_args
from bdf.models import User, General
from bdf.gen import bp
from bdf.gen.forms import AddGeneralForm
import time
import csv


@bp.route('/gen', methods=['GET', 'POST'])
@login_required
def gen():
    gens = General.query.order_by(General.id.asc())
    forms = []
    def get_forms(offset=0, per_page=20):
        return forms[offset: offset + per_page]
    for gen in gens:
        form = AddGeneralForm()
        form.id.default = gen.id
        form.name.default = gen.name
        forms.append(form)
    for form in forms:
        if form.validate_on_submit():
            if form.modify.data:
                gen = General.query.filter_by(id=form.id.data).one()
                gen.name = form.name.data
                db.session.add(gen)
                db.session.commit()
            elif form.delete.data:
                gen = General.query.filter_by(id=form.id.data).one()
                db.session.delete(gen)
                db.session.commit()
            return redirect(url_for('gen.gen'))
        form.process()  # Do this after validate_on_submit or breaks CSRF token
    page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
    total = len(forms)
    pagination_forms = get_forms(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('gen/gen.html', gens=gens, title=General,
                          page=page, forms=pagination_forms, per_page=per_page, pagination=pagination)



@bp.route('/gen/upload_gen', methods=['GET', 'POST'])
@login_required
def upload_gen():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            general = General(id=row[0], name=row[1])
            db.session.add(general)
            db.session.commit()
        return redirect(url_for('gen.gen'))
    return render_template('gen/upload_gen.html')

@bp.route('/gen/add_gen', methods=('GET', 'POST'))
@login_required
def add_gen():
    form = AddGeneralForm()
    if form.validate_on_submit():
        gen = General(id=form.id.data, name=form.name.data)
        db.session.add(gen)
        db.session.commit()
        flash('Congratulations, you have now a registered a new General!')
        return redirect(url_for('gen.gen'))
    return render_template('gen/add_gen.html', form=form)
