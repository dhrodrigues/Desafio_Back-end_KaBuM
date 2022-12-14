from fastapi import APIRouter, status,HTTPException
from typing import List
from models.pack import Pack


pack_router = APIRouter(tags=["Pack"])

pack =[]


@pack_router.post("/pack")
def Packs(data:Pack) -> dict:
    if data.id in pack:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Existente.")
