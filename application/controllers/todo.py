from sanic import request, response, Blueprint
from sanic.response import json
from playhouse.shortcuts import model_to_dict

from ..models import Todo


bp_todo = Blueprint('todo', url_prefix='todos')


@bp_todo.route('/')
async def index(request):
    data = await Todo.get()
    return json({'todos': model_to_dict(data)})


@bp_todo.route('/', methods=frozenset({'POST'}))
async def post(request):
    title = request.json.get('title')
    description = request.json.get('description')

    await Todo.create(title=title, description=description)

    return json({'success': True})
