import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def create_token(data:dict):
    token: str=jwt.encode(payload=data,key="secretkey",algorithm="HS256")
    return token

def validateToken(token:str):
    try:
        data:dict=jwt.decode(token,key="secretkey",algorithms={"HS256"})
        
    except ExpiredSignatureError:
        raise HTTPException(status_code=403,detail="Token Expirado")
    
    except InvalidTokenError:
        raise HTTPException(status_code=403,detail="Token no Autorizado")