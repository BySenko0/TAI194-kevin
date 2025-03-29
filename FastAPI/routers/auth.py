from typing import List
from fastapi import FastAPI, HTTPException
from modelsPydantic import modelAuth
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from fastapi import APIRouter


routerAuth = APIRouter()

#Endpoint para generar token
@routerAuth.post("/auth", tags=["Autenticacion"])
def auth(credenciales:modelAuth):
    if credenciales.mail == "kevin@gmail.com" and credenciales.passw == "123456789":
        token:str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse (content={"token": token})
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}