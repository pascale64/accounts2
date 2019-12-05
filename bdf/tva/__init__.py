from flask import Blueprint

bp = Blueprint('tva', __name__)

from bdf.tva import tva

