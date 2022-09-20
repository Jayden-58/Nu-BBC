from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')

@bp.route('', methods=['GET'])
def index():
    tweets = Tweet.query.all()
    result = []
    for t in tweets:
        result.append(t.serialize())
    return jsonify(result)