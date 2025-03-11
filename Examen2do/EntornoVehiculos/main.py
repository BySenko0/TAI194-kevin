from fastapi import FastAPI, HTTPException
from typing import Optional
from models import modelCarro


app = FastAPI(
    title="Examen Fast api",
    description="Vehiculos Examen tipo c",
    version="1.0.1"
)

Carros=[
    {"id":1, "modelo":"jetta", "año":2010, "placa":"abc123"},
    {"id":2, "modelo":"chevy", "año":2011, "placa":"def456"},
    {"id":3, "modelo":"aveo", "año":2012, "placa":"ghi789"},
    {"id":4, "modelo":"spark", "año":2013, "placa":"jkl012"},
    {"id":5, "modelo":"matiz", "año":2014, "placa":"mno345"}
]

@app.get("/", tags=["Inicio"])
def Home():
    return {"message": "centro vehicular"}

@app.get("/Carros", tags=["Operaciones CRUD"])
def leer():
    return Carros

@app.post("/Carros",response_model= modelCarro ,tags=["Operaciones agregar"])
def insert(carro: modelCarro):
    for car in Carros:
        if car["id"] == carro.id:
            raise HTTPException(status_code=400, detail="El carro ya existe")
    Carros.append(carro.dict())
    return carro

@app.delete("/Carros/{id}", tags=["Operaciones eliminar"])
def eliminar(id: int):
    for index, car in enumerate(Carros):
        if car["id"] == id:
            Carros.pop(index)
            return {"message": "Carro eliminado"}
    raise HTTPException(status_code=404, detail="El carro no existe")
