import uvicorn
from fastapi import FastAPI
from routes.freight import freight_router
from routes.pack import pack_router

app = FastAPI()

app.include_router(pack_router, prefix="/Pack")
app.include_router(freight_router, prefix="/Freight")        

        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8085, reload=True)
    