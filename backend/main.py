from fastapi import FastAPI
from routes.conversation import router

app = FastAPI(
    title="Personalized Networking Assistant API",
    version="1.0"
)

app.include_router(router)