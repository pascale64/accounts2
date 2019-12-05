from flask import Blueprint

bp = Blueprint('gen', __name__)

from bdf.gen import gen

