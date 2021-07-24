from fastapi import FastAPI
from app.routers.index import user, bank, province, login

app = FastAPI()

app.include_router(user, prefix="/user", tags=['user'])
app.include_router(bank, prefix="/bank", tags=['bank'])
app.include_router(province, prefix="/province", tags=['province'])
app.include_router(login, prefix="/login", tags=['login'])  
