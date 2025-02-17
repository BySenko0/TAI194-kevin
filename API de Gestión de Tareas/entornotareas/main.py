from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Gestión de Tareas",
    description="api para gestionar tareas",
    version="1.0.0"
)

# Base de datos simulada (Lista de tareas)
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-24", "estado": "completada"},
    {"id": 2, "titulo": "hacer un pan", "descripcion": "Hacer un pan", "vencimiento": "15-02-25", "estado": "completada"},
]

# a) Obtener todas las tareas
@app.get("/tareas", tags=["Operaciones CRUD"])
def obtener_tareas():
    return {"tareas": tareas}
