from fastapi import FastAPI
from domain.freight import freight_routes
from domain.pack import pack_routes



def setup_routes(app: FastAPI):
    app.include_router(pack_routes.router,tags=["Pacotes"], prefix="/packs")
    app.include_router(freight_routes.router,tags=["Fretes"], prefix="/fretes")