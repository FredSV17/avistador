from fastapi import FastAPI
from routes import api_router
from db.db_manager import drop_database
import os

from webscraper.webscraping_amazon import start_webscraping

app = FastAPI()

app.include_router(api_router)

from fastapi.middleware.cors import CORSMiddleware


# origins = [
#     "http://localhost",
#     "http://localhost:8000/*",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_description="Início")
async def hello():
    await start_webscraping("Televisão")
    return "Hello!"

@app.on_event("shutdown")
async def shutdown_remove_db():
    if os.environ["API_TEST"]:
        drop_database()