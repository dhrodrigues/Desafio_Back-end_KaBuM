import uvicorn
from fastapi import FastAPI
from models.freight_model import Fretes

app = FastAPI()
cargas =[] 

        
@app.post("/frete", response_model=bool, tags=["frete"])
def inf_frete(frete: Fretes):
    cargas.append(frete)   
    return True

@app.get("/list", response_model=list, tags=["list"])
def list_frete():
    return  cargas       
        
        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8085, reload=True)
    