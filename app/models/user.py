from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(255)),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(60)),
    Column('disabled', Integer),
)