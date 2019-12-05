from flask import Blueprint

bp = Blueprint('auth', __name__)

from bdf.auth import auth

