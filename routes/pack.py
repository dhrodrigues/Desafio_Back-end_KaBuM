from fastapi import APIRouter, status,HTTPException
from typing import List
from models.pack import Pack


pack_router = APIRouter(tags=["Type_Pack"])

pack =[]


@pack_router.get("/", response_model= List[Pack])
def get_all_pack() -> dict[Pack]:
    
    return pack

@pack_router.get("/{id}", response_model=Pack)
def get_one_package(id: int) -> Pack:
    for package in pack:
        if package.id == id:
            return package
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID não encontrado.")

# @pack_router.post("/pack")
#     def new_pack ()