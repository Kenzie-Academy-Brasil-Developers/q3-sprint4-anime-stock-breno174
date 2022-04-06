from flask import request, jsonify
from os import getenv
from dotenv import load_dotenv
from http import HTTPStatus
from psycopg2.errors import UniqueViolation

from app.models.anime_model import Animes

load_dotenv()


def all_animes():
    try:
        all_animes = Animes.all_animes()
    except(Exception):
        return {'msg': 'data base is empty', 'database': []}, 200

    serializer = [Animes.serialize_data(anime) for anime in all_animes]

    return jsonify(serializer), 200


def post_anime():
    data = request.json
    newanime = Animes(**data)

    try:
        insert_anime = newanime.create_anime()
        serielizer = Animes.serialize_data(insert_anime)
    except UniqueViolation:
        return {'error': 'anime already exist'}, 422

    return jsonify(serielizer), 201


def found_one_anime(anime_id):
    try:
        anime = Animes.one_anime(anime_id)
    except(Exception):
        return {"msg": "id nao encontrado no banco de dados"}, 404

    if not anime:
        return {"msg": "id nao encontrado no banco de dados"}, 404

    serializer = Animes.serialize_data(anime)

    return serializer, 200


def del_anime(anime_id):
    try:
        anime = Animes.dell_anime(anime_id)
    except (Exception):
        return {"msg": "id nao encontrado no banco de dados"}, 404
    
    if not anime:
        return {"msg": "id nao encontrado no banco de dados"}, 404
    
    serializer = Animes.serialize_data(anime)

    return serializer, 200


def patch_anime(anime_id):
    data = request.json
    update_anime = Animes.update_anime(anime_id, data)
    serializer = serializer = Animes.serialize_data(update_anime)

    return jsonify(serializer), 200
