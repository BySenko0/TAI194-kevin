from fastapi import FastAPI
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

@app.get("/promedio", tags=["Mi calificacion"])
def promedio():
    return 10.5

#para que sea obligatorio el endpoint
@app.get("/usuario/{id}", tags=["Endpoint Parametro obligatorio"])
def consultausuario(id: int):
    return {"se encontro el usuario: ": id}

#para que sea endpoint opcional
@app.get("/usuario/", tags=["Endpoint Parametro opcional"])
def consultausuario2(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usuario}
        return {"mensaje": f"no se encontro el usuario con el id {id}"}
    return {"mensaje": "no se proporciono el id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}