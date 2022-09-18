from flask import Blueprint, jsonify, abort, request
from ..models import Publisher

bp = Blueprint('publishers', __name__, url_prefix='/publishers')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    publishers = Publisher.query.all()  # ORM performs SELECT query
    result = []
    for p in publishers:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response