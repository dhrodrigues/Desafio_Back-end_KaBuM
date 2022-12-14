from fastapi import APIRouter, status,HTTPException
from models.freight_model import Freight

freight_router = APIRouter(tags=["Freightage"])

freights = [{
                "id": 1,
                "nome": "Entrega Ninja",
                "constante_calculo": 0.3,
                "altura_minima": 10,
                "altura_maxima": 200,
                "largura_minima": 6,
                "largura_maxima": 140,
                "prazo_entrega": "6 dias"

            },
            {
                "id": 1,
                "nome": "Entrega Kabum",
                "constante_calculo": 0.2,
                "altura_minima": 5,
                "altura_maxima": 140,
                "largura_minima": 13,
                "largura_maxima": 125,
                "prazo_entrega": "4 dias"

            }
]

@freight_router.post("/freightage")
def Freight(data:Freight) -> dict:
    if data.id in freights:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Existente.")

    freights[data.id] = data
    return {"mensagem": "Cadastro com Sucesso!"}


@freight_router.get("/Freight")
def Freight():
    return freights