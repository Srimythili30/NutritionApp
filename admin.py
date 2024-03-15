from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import User
from db import SessionLocal
import routers.schemas, routers.auth

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_dependency =Annotated[dict,Depends(routers.auth.get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/User", status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,
                   db: db_dependency):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(User).all()