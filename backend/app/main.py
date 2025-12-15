from fastapi import FastAPI
from .database import Base, engine
from .routers import categories, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(categories.router)
app.include_router(tasks.router)
