from flask import Blueprint

bp = Blueprint('stock', __name__)

from bdf.stock import stock

