import asyncio
import json

import uvloop
from sanic import Sanic
from sanic.log import log
from sanic_cors import CORS

from .database import database

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

__all__ = ['create_app']


def create_app():
    app = Sanic()

    configure_extensions(app)
    configure_listener(app)
    configure_views(app)

    return app


def configure_extensions(app):
    CORS(app)


def configure_listener(app):
    @app.listener('before_server_start')
    async def setup(app, loop):
        # create connection pool
        await database.connect(loop)

    @app.listener('before_server_stop')
    async def stop(app, loop):
        # close connection pool
        await database.close()

    @app.middleware('request')
    async def log_request_args(request):
        log.debug('Request args: {}'.format(json.dumps(request.args)))


def configure_views(app):
    from .controllers import bp_todo
    from .views import hello

    app.add_route(hello, '/')
    app.blueprint(bp_todo)
