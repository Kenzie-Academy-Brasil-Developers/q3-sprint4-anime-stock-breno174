from flask import Blueprint

bp_patch = Blueprint('patch', __name__)

bp_patch.patch('/<anime_id>')()
