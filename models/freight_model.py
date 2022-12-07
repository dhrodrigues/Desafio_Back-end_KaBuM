from pydantic import BaseModel

class Freight(BaseModel):
    id: int
    nome: str
    constante_calculo: float
    altura_minima: int
    altura_maxima: int
    largura_minima: int
    largura_maxima: int
    prazo_entrega: str

    class Type_freight:
        schema_extra = {
            "example": {
                "id": 1,
                "nome": "Entrega Kabum",
                "constante_calculo": 0.2,
                "altura_minima": 5,
                "altura_maxima": 140,
                "largura_minima": 13,
                "largura_maxima": 125,
                "prazo_entrega": "4 dias"

            }
        }