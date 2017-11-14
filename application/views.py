from sanic.response import json, html


async def hello(request):
    return json({'message': 'hello'})
