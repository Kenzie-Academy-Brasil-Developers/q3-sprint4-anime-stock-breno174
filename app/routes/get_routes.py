from flask import Blueprint
from app.controllers.animes_controls import all_animes, found_one_anime

bp_get = Blueprint('get', __name__)

bp_get.get('')(all_animes)
bp_get.get('/<anime_id>')(found_one_anime)
