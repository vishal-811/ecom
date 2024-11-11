from sqlmodel import SQLModel, Session, create_engine 


DATABASE_URL = "postgresql://postgres:admin@postgres:5432/mydatabase"
engine = create_engine(DATABASE_URL, echo = False)


def init_db():
    print("here in a db")
    try:
        SQLModel.metadata.create_all(engine)
        print("Tables created in a db")
    except Exception as e :
        print(f"Failed to create a table in the db , {e}")

    

def get_session():
    try :
         session = Session(engine)
         yield session
    finally:
        session.close()


