from typing import List
from fastapi import FastAPI, HTTPException
from modelsPydantic import modelUsuario
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
    title="Mi primer API",
    description="Victor O.O",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

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

# Endpoint GET - Obtener todos los usuarios
@app.get("/todoUsuarios", response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def leer():
    db=Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content = jsonable_encoder(consulta))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "El usuario no se puede guardar", "error": str(e)})
    finally:
        db.close()

# Endpoint POST - Insertar usuario
@app.post("/Usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"], responses={
    400: {"description": "El usuario ya existe"}
})
def insert(usuario: modelUsuario):
    db = Session()
    try:
        db_user = User(
            name=usuario.nombre,  # Ahora usa "name"
            age=usuario.edad,  # Ahora usa "age"
            email=usuario.correo  # Ahora usa "email"
        )
        db.add(db_user)
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario creado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "El usuario no se puede guardar", "error": str(e)})
    finally:
        db.close()

# Endpoint GET - Buscar un solo usuario por ID
@app.get("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def leeruno(id: int):
    db = Session()
    try:
        consulta1 = db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={"mensaje": "usuario no encontrado"})

        return JSONResponse(content=jsonable_encoder(consulta1))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar usuario: {str(e)}")
    finally:
        db.close()
 

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
