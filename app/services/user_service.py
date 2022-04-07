from functools import wraps
from http import HTTPStatus
import http
from flask import request


TRUSTHED_KEYS = [
            "id",
            "anime",
            "released_date",
            "seasons"
        ]


def validate_keys():
    keys = list(request.json.keys())
    expected = TRUSTHED_KEYS
    for key in keys:
        if key not in expected:
            return {
                "error": "chave(s) incorreta(s)",
                "expected": expected,
                "received": list(request.json),
            }, HTTPStatus.UNPROCESSABLE_ENTITY


def verify_keys_decorator():
    def receive_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            try:
                data["id"]
                data["anime"]
                data["released_date"]
                data["seasons"]

            except KeyError:
                return {
                    "error": "chave(s) incorreta(s)",
                    "expected": TRUSTHED_KEYS,
                    "received": list(data.keys()),
                }, HTTPStatus.BAD_REQUEST

            result = func(*args, **kwargs)

            return result

        return wrapper

    return receive_func

def cash_keys(payload: dict):
        for key in payload.keys():
            if type(payload[key]) == str:
                payload[key] = payload[key].lower().title()
        return payload
