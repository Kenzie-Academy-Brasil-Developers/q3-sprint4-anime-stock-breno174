from flask import Blueprint
from app.controllers.animes_controls import del_anime

bp_delete = Blueprint('delete', __name__)

bp_delete.delete('/<anime_id>')(del_anime)
