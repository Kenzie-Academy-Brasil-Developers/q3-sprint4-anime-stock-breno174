from flask import Flask, Blueprint
from .get_routes import bp_get
from .delete_routes import bp_delete
from .post_routes import bp_post
from .patch_routes import bp_patch
from app.models.anime_model import Animes

bp_anime = Blueprint('animes', __name__, url_prefix='/animes')


def init_app(app: Flask):
    Animes.create_db()
    
    bp_anime.register_blueprint(bp_get)
    bp_anime.register_blueprint(bp_post)
    bp_anime.register_blueprint(bp_patch)
    bp_anime.register_blueprint(bp_delete)

    app.register_blueprint(bp_anime)
