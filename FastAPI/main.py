from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Mi primer API con FastAPI",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)

class ModelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

# Lista de usuarios
usuarios = [
    {"id": 1, "nombre": "kevin", "edad": 20, "correo": "uwu@gmail.com"},
    {"id": 2, "nombre": "jose", "edad": 30, "correo": "owo@gmail.com"},
    {"id": 3, "nombre": "maria", "edad": 40, "correo": "ewe@gmail.com"},
    {"id": 4, "nombre": "luis", "edad": 50, "correo": "waos@gmail.com"},
    {"id": 5, "nombre": "juan", "edad": 60, "correo": "uwu2@gmail.com"},
]

@app.get("/", tags=["Inicio"])
def home():
    return {"message": "Hello, FastAPI!"}

# Endpoint para obtener todos los usuarios
@app.get("/todosUsuarios", response_model=List[ModelUsuario], tags=["Operaciones CRUD"])
def leer():
    return usuarios  # Se devuelve directamente la lista, sin un diccionario

# Endpoint para agregar un nuevo usuario
# Endpoint POST
@app.post("/Usuarios/", response_model=ModelUsuario, tags=["Operaciones CRUD"])
def insert(usuario: ModelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:  # Corrección aquí
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario.dict())  # Convertimos el objeto en un diccionario antes de agregarlo a la lista
    return usuario


# Endpoint para actualizar un usuario por ID
@app.put("/Usuarios/{id}", response_model=ModelUsuario, tags=["Operaciones CRUD"])
def actualizar(id: int, usuarioActualizado: ModelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado  # Se almacena directamente el objeto Pydantic
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no existe")


# Endpoint para eliminar un usuario por ID
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuario_eliminado = usuarios.pop(index)
            return {"message": "Usuario eliminado", "usuario": usuario_eliminado}
    raise HTTPException(status_code=404, detail="El usuario no existe")
