from pydantic import BaseModel, Field, EmailStr

class ModelUsuario(BaseModel):  # Cambio en la M mayúscula
    id: int = Field(..., gt=0, description="Id siempre debe ser positivo")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios, min 1 max 85")
    edad: int = Field(..., ge=1, le=99, description="Edad mínima 1, máxima 99")  # Se corrige min_length/max_length
    correo: str = Field(..., pattern=r"^.@.com$", description="Correo válido",example="usuario@example.com")  # Se cambia regex por pattern

class ModelAuth(BaseModel):
    correo: EmailStr
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="solo letras sin espacios min 8",example="")