from pydantic import BaseModel, Field

class modelCarro(BaseModel): 
    id: int = Field(..., gt=0, description="Id siempre debe ser positivo")
    modelo: str = Field(..., min_length=1, max_length=25, description="Solo letras y espacios, min 1 max 25")
    año: int = Field(..., ge=1000, le=3000, description="Año int min 4 digitos")
    placa: str = Field(..., min_length=1, max_length=10, description="Placa min 1 max 7")
     
