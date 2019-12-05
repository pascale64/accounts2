import os
basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://accounting:topdog@localhost/account'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS_DEFAULT_DEST = basedir + '/static/img/'
    UPLOADS_DEFAULT_URL = 'http://192.168.0.11/static/img/'
    UPLOADED_IMAGES_DEST = basedir + '/static/img/'
    UPLOADED_IMAGES_URL = 'http://192.168.0.11/static/img/'
    ITEMS_PER_PAGE = 25
