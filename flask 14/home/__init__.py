from flask import Blueprint

home_bp = Blueprint('home', __name__)

from . import routes  # Import routes so they get registered