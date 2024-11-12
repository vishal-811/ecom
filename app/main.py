from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
import uvicorn
from api.authRoutes import authRouter
from api.adminRoutes import adminRoutes
from api.userRoutes import userRoutes
from db.database import init_db
from api.userMiddleware import userMiddleware


@asynccontextmanager
async def lifespan(app:FastAPI):
    try:
        print("connection Started")
        init_db()
        print("connection done")
        yield
    
    finally:
        print("Code Runn Sucess")
        pass

app = FastAPI(
    lifespan=lifespan
)



@app.get("/")
def hello():
    return "hello"

@app.middleware('http')
async def check_user_middleware(request : Request, call_next):
   try:
        protected_routes = ['/buy', '/checkout', '/order']
        if any(request.url.path.startswith(route) for route in protected_routes):
         print("fine1")
         auth_response= await userMiddleware(request)
         if auth_response is not None :
          return await call_next(request)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
   except Exception as error :
       print("fine2")
       raise HTTPException(status_code=401, detail="auth  failed")
    

app.include_router(authRouter, tags=["auth"]) 
app.include_router(adminRoutes, tags=["admin"])
app.include_router(userRoutes,tags=["user"])


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)