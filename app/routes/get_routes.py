from flask import Blueprint

bp_get = Blueprint('get', __name__)

bp_get.get('')()
bp_get.get('/<anime_id>')()