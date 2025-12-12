from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, routes


app = FastAPI(title="Warranty Register API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://asset-management-prixxb6d4-mutinhiris-projects.vercel.app"],  # or ["https://server4.eport.ws"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Include routes
app.include_router(routes.router)
