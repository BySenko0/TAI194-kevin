from DB.conexion import Base
from sqlalchemy import	Column,Integer,String

class User(Base):
    __tablename__ = "tbUsers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(85), nullable=False)  # Cambiado de 'nombre' a 'name'
    age = Column(Integer, nullable=False)  # Cambiado de 'edad' a 'age'
    email = Column(String, unique=True, nullable=False)  # Cambiado de 'correo' a 'email'
    password = Column(String, nullable=False)  # Agregado para coincidir con la BD