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

# Obtener una tarea específica por su ID
@app.get("/tareas/{id}", tags=["Operaciones CRUD"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Crear una nueva tarea
@app.post("/tareas", tags=["Operaciones CRUD"])
def agregar_tarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El ID de la tarea ya existe")
    tareas.append(tarea)
    return tarea

