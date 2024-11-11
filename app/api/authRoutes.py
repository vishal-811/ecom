from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session, select
from db.models import User
from models.schema import Create_user, SigninSchema
from db.database import get_session
from passlib.context import CryptContext

authRouter = APIRouter()

SessionDep =  Annotated[Session,Depends(get_session)]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@authRouter.post('/signup')
def signup(data : Create_user, db : SessionDep ) :
    alreadyExist = db.exec(select(User).where(User.username == data.username)).first()

    if alreadyExist :
      raise HTTPException(status_code=401 , detail ="User already exist with this credentials")
    
    print("The hashed password is", data.password)
    hashedpassword = pwd_context.hash(data.password)

    new_user = User(username = data.username ,
                    password = hashedpassword,
                    role = data.role.value
                   )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return { "msg" :"Signup SuccessFul"}


@authRouter.post('/signin')
def signin(data : SigninSchema , db : SessionDep) :
    username = data.username
    userDetails = db.exec(select(User).where(User.username == username)).first()
    if not userDetails:
        raise HTTPException(status_code= 401 , detail ="No user exist with this credentails")
    isValidPass = pwd_context.verify(data.password,userDetails.password)
    if not isValidPass :
        raise HTTPException(status_code=401, detail ="Wrong password")
    print("6")

    return{"msg" :"Signin sucess"} 


    

     
    
