from sqlmodel import SQLModel,Field

class User(SQLModel,table = True):
    id: int | None = Field(index=True, primary_key=True)
    username : str
    password : str 
    role : str
