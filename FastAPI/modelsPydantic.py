from pydantic import BaseModel, EmailStr, Field

class modelUsuario(BaseModel): 
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios, min 1 max 85")
    edad: int = Field(..., ge=1, le=99, description="Edad mínima 1, máxima 99")  
    correo: EmailStr = Field(..., description="Correo válido", example="usuario@example.com")
 

class modelAuth(BaseModel):
    mail : EmailStr 
    passwd: str = Field(..., min_length=8, strip_whitespace=True , description="La contraseña es de minimo 8 caracteres sin letras y espacios")