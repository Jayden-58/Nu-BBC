from flask import Blueprint, jsonify, abort, request
from ..models import Song

bp = Blueprint('songs', __name__, url_prefix='/songs')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    songs = Song.query.all()  # ORM performs SELECT query
    result = []
    for s in songs:
        result.append(s.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response