from sqlalchemy import Column, ForeignKey
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Integer, String
from db import Base
from routers.schemas import UserLevel  # corrected import statement


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    age = Column(Integer)
    level = Column(SQLEnum(UserLevel))
    role = Column(String)

class UserResponse(Base):

    __tablename__ ="UserResponse"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,ForeignKey("users.username"))
    response = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"))
    query = Column(String)
    
    