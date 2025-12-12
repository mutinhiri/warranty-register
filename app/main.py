from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, routes


app = FastAPI(title="Warranty Register API")


origins = [
    "https://asset-management-git-dev-mutinhiris-projects.vercel.app",
    "https://server4.eport.ws",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # cannot use "*" with credentials
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Include routes
app.include_router(routes.router)
