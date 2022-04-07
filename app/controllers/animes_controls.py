from flask import request, jsonify
from os import getenv
from dotenv import load_dotenv
from http import HTTPStatus
from psycopg2.errors import UniqueViolation, ProgrammingError

from app.models.anime_model import Animes
from app.services.user_service import validate_keys

load_dotenv()


def all_animes():
    try:
        all_animes = Animes.all_animes()
    except(Exception):
        return {'msg': 'data base is empty', 'database': []}, 200

    serializer = [Animes.serialize_data(anime) for anime in all_animes]

    return jsonify(serializer), 200


def post_anime():
    if validate_keys():
        return validate_keys()

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
    anime = Animes.dell_anime(anime_id)
    
    if not anime:
        return {"msg": "id nao encontrado no banco de dados"}, 404

    return '', 200


def patch_anime(anime_id):
    if validate_keys():
        return validate_keys()

    data = request.json
    try:
        update_anime = Animes.update_anime(anime_id, data)
    except ProgrammingError:
        return {"msg": "id nao encontrado no banco de dados"}, 404
    serializer = serializer = Animes.serialize_data(update_anime)

    return jsonify(serializer), 200
