from fastapi import FastAPI
from app.routers import user_router

app = FastAPI(title="My API")

app.include_router(user_router.router)