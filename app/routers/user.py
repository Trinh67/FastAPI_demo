from fastapi import APIRouter

from config.db import conn
from app.models.index import users
from app.schemas.index import User
from passlib.context import CryptContext

user = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()


@user.get('/{id}')
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post('/')
async def write_data(user: User):
    hashed_password = pwd_context.hash(user.password)
    conn.execute(users.insert().values(
        username=user.username,
        name=user.name,
        email=user.email,
        password=hashed_password,
        disabled=user.disabled,
    ))
    return conn.execute(users.select()).fetchall()


@user.put('/{id}')
async def update_data(id: int, user: User):
    hashed_password = pwd_context.hash(user.password)
    conn.execute(users.update().values(
        username=user.username,
        name=user.name,
        email=user.email,
        password=hashed_password,
        disabled=user.disabled,
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.delete('/{id}')
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()