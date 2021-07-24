from fastapi import APIRouter
from config.db import data_config

bank = APIRouter()

banks = data_config["banks"]

@bank.get('/')
def read_data():
    return banks

@bank.get('/{code}}')
def read_data(code: str):
    return [x for x in banks if x['bankCode'].upper() == code.upper()]
