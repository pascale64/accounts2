from flask import Blueprint

bp = Blueprint('uploads', __name__)

from bdf.uploads import uploads

