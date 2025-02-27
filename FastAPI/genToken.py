import jwt

def create_token(data: dict):
    token: str = jwt.encode(payload=data
                            , key="secretkey"
                            , algorithm="HS256")
    return token