from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()
cargas =[] 

class Fretes(BaseModel):
    id: int
    nome: str
    constante_calculo: float
    altura_minima: int
    altura_maxima: int
    largura_minima: int
    largura_maxima: int
    prazo_entrega: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nome": "Entrega Ninja",
                "constante_calculo": 0.3,
                "altura_minima": 10,
                "altura_maxima": 200,
                "largura_minima": 6,
                "largura_maxima": 140,
                "prazo_entrega": "6 dias"

            }
        }
        
@app.post("/frete", response_model=bool, tags=["frete"])
def create_login(frete: Fretes):
    cargas.append(frete)   
    return True

@app.get("/list", response_model=list, tags=["list"])
def list_users():
    return  cargas       
        
        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8085, reload=True)
    