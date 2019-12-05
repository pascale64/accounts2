from flask import Blueprint

bp = Blueprint('aux', __name__)

from bdf.aux import aux

