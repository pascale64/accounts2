from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from bdf import db
from bdf.models import User, Book, Auxilliere, General, Type, Period_id, Journal,\
                       Stock, Sale, Clients, Bordeauxbrocante, Froufrou, Amazon, PayPal
from bdf.uploads import bp
import time



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/uploads', methods=['GET', 'POST'])
@login_required
def uploads():
    books = Book.query.all()
    return render_template('uploads/uploads.html', books=books)
    

    
@bp.route('/uploads/upload_type', methods=['GET', 'POST'])
@login_required
def upload_type():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            typ = Type(id=row[0], name=row[1])
            db.session.add(typ)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_type.html')
    
@bp.route('/uploads/upload_pid', methods=['GET', 'POST'])
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
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_pid.html')
    
@bp.route('/uploads/upload_jn', methods=['GET', 'POST'])
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
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_jn.html')
    
@bp.route('/uploads/upload_stock', methods=['GET', 'POST'])
@login_required
def upload_stock():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            stock = Stock(id=row[0], name=row[1])
            db.session.add(stock)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_stock.html')
    
@bp.route('/uploads/upload_sto', methods=['GET', 'POST'])
@login_required
def upload_sto():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            stock = Stock(id=row[0], name=row[1])
            db.session.add()
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_.html')
    
@bp.route('/uploads/upload_bb', methods=['GET', 'POST'])
@login_required
def upload_bb():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            bb = Bordeauxbrocante(id=row[3], date=row[21], buyer=row[2], avantcomm=row[4],
            comm=row[5], net=row[6], rate=row[16], REM=row[10], Remcomm=row[11])
            db.session.add(bb)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_bb.html')
    
@bp.route('/uploads/upload_ff', methods=['GET', 'POST'])
@login_required
def upload_ff():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ff = Froufrou(id=row[3], date=row[21], buyer=row[2], avantcomm=row[4],
            comm=row[5], net=row[6], rate=row[16], REM=row[10], Remcomm=row[11])
            db.session.add(ff)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_ff.html')
    
@bp.route('/uploads/upload_am', methods=['GET', 'POST'])
@login_required
def upload_am():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            am = Amazon(id=row[3], date=row[0], avantcomm=row[12],
            comm=row[18], net=row[22])
            db.session.add(am)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_am.html')
    
@bp.route('/uploads/upload_client_bb', methods=['GET', 'POST'])
@login_required
def upload_client_bb():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            client = Clients(name=row[17], Add_1=row[18], Add_2=row[19], Ville=row[20], Region=row[21],
            CodePostale=row[22], Pays=row[23])
            db.session.add(client)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_client_bb.html')
    
@bp.route('/uploads/upload_client_ff', methods=['GET', 'POST'])
@login_required
def upload_client_ff():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            client = Clients(name=row[17], Add_1=row[18], Add_2=row[19], Ville=row[20], Region=row[21],
            CodePostale=row[22], Pays=row[23])
            db.session.add(client)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_client_ff.html')
    
@bp.route('/uploads/upload_client_am', methods=['GET', 'POST'])
@login_required
def upload_client_am():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            amazon = Amazon(name=row[0], Add_1=row[1], Add_2=row[2], Ville=row[3], Region=row[4],
            CodePostale=row[5], Pays=row[6])
            db.session.add(amazon)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_client_.html')
    
@bp.route('/uploads/upload_sales_bb', methods=['GET', 'POST'])
@login_required
def upload_sales_bb():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            bb = Bordeauxbrocante(trans=row[13], buyer=row[17], pays=row[23], QT=row[3],
             prix_de_vente=row[4], poste=row[9], bordeaux=row[24], date=row[0], description=row[1])
            db.session.add(bb)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_sales_bb.html')
    
@bp.route('/uploads/upload_sales_ff', methods=['GET', 'POST'])
@login_required
def upload_sales_ff():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            ff = Froufrou(trans=row[13], buyer=row[17], pays=row[23], QT=row[3],
                    prix_de_vente=row[4], poste=row[9], frou=row[24], date=row[0], description=row[1])
            db.session.add(ff)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_sales_ff.html')
    
@bp.route('/uploads/upload_sales_am', methods=['GET', 'POST'])
@login_required
def upload_sales_am():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            am = Amazon(trans=row[1], buyer=row[5], pays=row[23], QT=row[9], poste=row[13],
             total=row[2], amazon=row[1], date=row[2], description=row[8])
            db.session.add(am)
            db.session.commit()
        return redirect(url_for('uploads.uploads'))
    return render_template('uploads/upload_sales_am.html')

