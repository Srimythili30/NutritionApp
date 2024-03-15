from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
import models
from routers import  schemas, security
from db import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
# ALGORITHM = 'HS256'
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def get_user(db:Session, username: str):
    user =db.query(models.User).filter(models.User.username == username).first()
    return user
    



async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    
    
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get('sub')
        id: int = payload.get('id')
        role: str = payload.get('role')
        if username is None :
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
        user = get_user(db, username=token_data.username)
        return {'username': username, 'id': id, 'role': role}
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
    
    