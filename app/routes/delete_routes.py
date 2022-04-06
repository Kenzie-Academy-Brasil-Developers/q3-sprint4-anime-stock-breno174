from flask import Blueprint

bp_delete = Blueprint('delete', __name__)

bp_delete.delete('/<anime_id>')()
