from fastapi import FastAPI
from . import models, database, routes

app = FastAPI(title="Warranty Register API")

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Include routes
app.include_router(routes.router)
