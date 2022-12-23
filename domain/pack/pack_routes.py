from fastapi import APIRouter, status,HTTPException
from domain.pack.pack_model import Pack
from typing import List

router = APIRouter()
pack =[]



@router.post("/pack", status_code=status.HTTP_201_CREATED)
def new_package(packs:Pack) -> dict:
    for package in pack:
        if packs.id == package.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Pacote existente.")
    pack.append(packs)

@router.get("/listpack")
def lista():
    return pack
