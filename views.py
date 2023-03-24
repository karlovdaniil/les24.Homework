from typing import Union

from flask import Blueprint, jsonify, request, Response
from typing import Optional
from marshmallow import ValidationError

from builder import build_query
from model import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, tuple[Response, int]]:
    data = request.json
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result: Optional[list[str]] = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=validated_data['file_name'],
            data=result,
        )

    return jsonify(result)


@main_bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'
