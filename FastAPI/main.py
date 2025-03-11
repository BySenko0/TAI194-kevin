from typing import List
from fastapi import FastAPI, HTTPException , Depends
from models import modelAuth, modelUsuario
from genToken import create_token
from fastapi.responses import JSONResponse
from middlewares import BearerJWT

app = FastAPI(
    title="Mi primer API",
    description="Victor O.O",
    version="1.0.1"
)

# Lista de usuarios simulando una BD
usuarios = [
    {"id": 1, "nombre": "Victor", "edad": 20, "correo": "victor@gmail.com"},
    {"id": 2, "nombre": "Oscar", "edad": 22, "correo": "oscar@gmail.com"},
    {"id": 3, "nombre": "Juan", "edad": 23, "correo": "juan@gmail.com"},
    {"id": 4, "nombre": "Pedro", "edad": 24, "correo": "pedro@gmail.com"},
    {"id": 5, "nombre": "Maria", "edad": 25, "correo": "maria@gmail.com"},
]

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def Home():
    return {"message": "Bienvenido a mi API"}

#Endpoint para generar tok
@app.post("/auth", tags=["Autenticacion"])
def auth(credenciales:modelAuth):
    if credenciales.mail == "kevin@example.com" and credenciales.passwd == "123456789":
        token:str = create_token(credenciales.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}

# Endpoint GET - Obtener todos los usuarios
@app.get("/todoUsuarios", dependencies= [Depends(BearerJWT())],response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def leer():
    return usuarios 

# Endpoint POST - Insertar usuario
@app.post("/Usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"], responses={
    400: {"description": "El usuario ya existe"}
})
def insert(usuario: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario.model_dump())  # Convertir a diccionario antes de agregar
    return usuario

# Endpoint PUT - Actualizar usuario
@app.put("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def actualizar(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()  # Convertir a dict
            return usuario_actualizado
    raise HTTPException(status_code=404, detail="El usuario no existe")

# Endpoint DELETE - Eliminar usuario
@app.delete("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def eliminar(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"message": "Usuario eliminado", "usuario": usr}
    raise HTTPException(status_code=404, detail="El usuario no existe")