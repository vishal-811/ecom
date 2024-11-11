from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api.authRoutes import authRouter
from api.adminRoutes import adminRoutes
from api.userRoutes import userRoutes
from db.database import init_db



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
    title="mY fast app",
    lifespan=lifespan
)



@app.get("/")
def hello():
    return "hello"



app.include_router(authRouter, tags=["auth"])
app.include_router(adminRoutes, tags=["admin"])
app.include_router(userRoutes,tags=["user"])


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)