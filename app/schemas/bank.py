from pydantic import BaseModel

class Bank(BaseModel):
    bankCode: str
    bankName: str