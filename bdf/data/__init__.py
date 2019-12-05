from flask import Blueprint

bp = Blueprint('sales', __name__)

from bdf.sales import sales

