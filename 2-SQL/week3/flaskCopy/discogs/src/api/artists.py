from flask import Blueprint, jsonify, abort, request
from ..models import Artist

bp = Blueprint('artist', __name__, url_prefix='/artists')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    artists = Artist.query.all()  # ORM performs SELECT query
    result = []
    for a in artists:
        result.append(a.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response