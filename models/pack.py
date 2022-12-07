from pydantic import BaseModel
from typing import Dict

class Pack(BaseModel):
    id: int
    dimensoes: Dict [str, int]
    peso: int


    class Type_pack:
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