import datetime
from aiopeewee import AioModel
from peewee import IntegerField, CharField, DateTimeField

from .database import database


class Todo(AioModel):
    class Meta:
        database = database
        db_table = 'todos'

    id = IntegerField(primary_key=True)
    title = CharField(max_length=32)
    description = CharField(max_length=512)
    created_at = DateTimeField(default=datetime.datetime.now())
