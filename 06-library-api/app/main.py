from fastapi import FastAPI
from  app.routers.routers import get_router

app = FastAPI()

app.include_router(get_router())