from pydantic import BaseModel
from enum import Enum

class Role(Enum):
    user ="user"
    admin ="admin"

class Create_user(BaseModel) :
    username : str
    password : str
    role : Role 


class SigninSchema(BaseModel):
    username : str
    password : str
    role : str

class BuyProductSchema(BaseModel):
    productId : int 
    quantity : int

