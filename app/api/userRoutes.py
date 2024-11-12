from fastapi import APIRouter,Depends,HTTPException
from models.schema import BuyProductSchema
from db.database import Session,get_session
from typing import Annotated
from sqlmodel import select
from db.models import Product
from api.userMiddleware import userMiddleware
userRoutes = APIRouter()

SessionDep =  Annotated[Session,Depends(get_session)]



@userRoutes.post('/buy')
async def buy_product(data : BuyProductSchema, db : SessionDep) :
 isValidProductId =db.exec(select(id).where(Product.id == data.productid)) 
 if not isValidProductId :
  raise HTTPException(status_code=401, detail="No product found with this id")

 if data.quantity <= 0 :
   raise HTTPException(status_code=401, detail="Please Specify a valid order quantity")
 
 db.exec()
