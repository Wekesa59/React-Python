import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class SuperHero(BaseModel):
    name: str

class SuperHeroes(BaseModel):
    superHeroes: List[SuperHero]

app = FastAPI()

origins = [
    "http://localhost:5173",
]

#Ensure that any commands or info comes from our origins address and not anywhere else
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Will not persist across server restarts
memory_db = {"superHeroes": []}

@app.get("/superHeroes", response_model=SuperHeroes)
def get_superHeroes():
    return SuperHeroes(superHeroes=memory_db["superHeroes"])

@app.post("/superHeroes")
def add_superHero(superHero: SuperHero):
    memory_db["superHeroes"].append(superHero)
    return superHero

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
