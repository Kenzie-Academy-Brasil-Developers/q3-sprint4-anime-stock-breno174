from flask import Blueprint
from app.controllers.animes_controls import post_anime

bp_post = Blueprint('post', __name__)

bp_post.post('')(post_anime)
