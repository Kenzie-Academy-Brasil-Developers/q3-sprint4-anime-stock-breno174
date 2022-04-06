from flask import Blueprint

bp_post = Blueprint('post', __name__)

bp_post.post('')()
