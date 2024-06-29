# database.py
from sqlmodel import SQLModel, create_engine, Session
from .models import TodoItem

#DATABASE_URL = "sqlite:///./todos.db"
# this is connection to your database
DATABASE_URL = 'postgresql://neondb_owner:pKwChBb6ckO8@ep-rapid-cloud-a5di1nqh.us-east-2.aws.neon.tech/neondb?sslmode=require'
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session