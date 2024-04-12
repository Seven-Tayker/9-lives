from flask import Blueprint, request, Response

from controllers.category import *
from models.exceptions import ModelNotFoundError

categories_view = Blueprint('categories', __name__, url_prefix='/categories')

@subjects_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_categories()
    else:
        submitted_data = request.POST

        return Response(save_category(submitted_data['name']), status=201)

@subjects_view.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def get_or_update_instance(id):
    if request.method == 'GET':
        try:
            return get_category_with_id(id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.PATCH
        return Response(save_category(name=data['name']), status=201)
    elif request.method == 'DELETE':
        return Response(delete_category(id), status=201)
