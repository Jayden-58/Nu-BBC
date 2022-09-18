from flask import Blueprint, jsonify, abort, request
from ..models import Album

bp = Blueprint('albums', __name__, url_prefix='/albums')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    albums = Album.query.all()  # ORM performs SELECT query
    result = []
    for a in albums:
        result.append(a.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response