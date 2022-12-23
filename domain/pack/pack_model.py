from pydantic import BaseModel
from typing import Dict

class Pack(BaseModel):
    id: int
    dimensoes: Dict [str, int]
    peso: float


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "dimensoes":{
                    "altura": 102,
                    "largura": 40
                },
                "peso":400
            }
        }