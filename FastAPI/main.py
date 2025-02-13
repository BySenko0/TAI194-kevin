from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API con FastAPI",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)

usuarios=[
    {"id":1, "nombre":"kevin", "edad":20},
    {"id":2, "nombre":"jose", "edad":30},
    {"id":3, "nombre":"maria", "edad":40},
    {"id":4, "nombre":"luis", "edad":50},
    {"id":5, "nombre":"juan", "edad":60},

]

@app.get("/", tags=["inicio"])
def home():
    return {"message": "Hello, FastAPI!"}

#Endpoint para obtener todos los usuarios
@app.get("/todosUsuarios", tags=["Operaciones Crud"])
def leer():
    return {"Usuarios registrados": usuarios}

#Endpoint para obtener todos los usuarios
@app.post("/Usuarios/", tags=["Operaciones Crud"])
def insert(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#Endpoint para obtener un usuario por su id
@app.put("/Usuarios/{id}", tags=["Operaciones Crud"])
def actualizar(id: int, usuarioActualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no existe")


@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="El usuario no existe")
