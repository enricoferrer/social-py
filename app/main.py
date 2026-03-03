from fastapi import FastAPI
from app.routers import user_router, post_router, comment_router

app = FastAPI(title="Social API")

app.include_router(user_router.router)
app.include_router(post_router.router)
app.include_router(comment_router.router)