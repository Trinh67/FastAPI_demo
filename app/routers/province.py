from fastapi import APIRouter
from config.db import data_config

province = APIRouter()

provinces = data_config["provinces"]

@province.get('/')
def read_data():
    return provinces

@province.get('/{code}}')
def read_data(code: str):
    return [x for x in provinces if x['provinceCode'].upper() == code.upper()]
