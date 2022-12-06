from pydantic import BaseModel
from typing import Dict

class Fretes(BaseModel):
    id: int
    dimensoes: Dict [str, int]
    peso: int


    class Config:
        schema_extra = {
            "teste": {
                "id": 1,
                "dimensoes":{
                    "altura": 102,
                    "largura": 40
                },
                "peso":400
            }
        }