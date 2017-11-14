from aiopeewee import AioMySQLDatabase

from config import db


database = AioMySQLDatabase(**db)
