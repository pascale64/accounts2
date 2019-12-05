import os
import RPi.GPIO as GPIO
from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf import FlaskForm
from datetime import timedelta
from flask_uploads import UploadSet, IMAGES, configure_uploads

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
images = UploadSet('images', IMAGES)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)
    app.config['UPLOAD_FOLDER'] = '/var/www/accounts/static/img'

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    configure_uploads(app, images)

    from bdf.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from bdf.aux import bp as aux_bp
    app.register_blueprint(aux_bp)
    
    from bdf.bilan import bp as bilan_bp
    app.register_blueprint(bilan_bp)
    
    from bdf.books import bp as books_bp
    app.register_blueprint(books_bp)

    from bdf.data import bp as data_bp
    app.register_blueprint(data_bp)
    
    from bdf.gen import bp as gen_bp
    app.register_blueprint(gen_bp)
    
    from bdf.sales import bp as sales_bp
    app.register_blueprint(sales_bp)
    
    from bdf.stock import bp as stock_bp
    app.register_blueprint(stock_bp)
    
    from bdf.tva import bp as tva_bp
    app.register_blueprint(tva_bp)
    
    from bdf.uploads import bp as uploads_bp
    app.register_blueprint(uploads_bp)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

