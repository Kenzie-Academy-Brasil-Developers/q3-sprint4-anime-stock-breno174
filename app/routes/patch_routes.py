from flask import Blueprint
from app.controllers.animes_controls import patch_anime

bp_patch = Blueprint('patch', __name__)

bp_patch.patch('/<anime_id>')(patch_anime)
