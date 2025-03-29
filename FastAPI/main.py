from fastapi import FastAPI
from DB.conexion import Base, engine
from routers.usuarios import routerUsuario
from routers.auth import routerAuth  # Importación correcta del router

app = FastAPI(
    title="Mi primer API",
    description="kevin",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

# Registro de rutas
app.include_router(routerUsuario)
app.include_router(routerAuth)  # ✅ Esto es necesario

@app.get("/", tags=["Inicio"])
def Home():
    return {"message": "Bienvenido a mi API"}
