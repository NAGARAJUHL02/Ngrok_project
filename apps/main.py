from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import user_routes

# Create database tables automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ngrok Project API")

# Include routers
app.include_router(user_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Ngrok Project API"}
