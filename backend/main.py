import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Superhero(BaseModel):
    name: str

class Superheroes(BaseModel):
    superheroes: List[Superhero]

app = FastAPI()

origins = [
    "https://localhost:5173"
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
memory_db = {"superheroes": []}

@app.get("/superheroes", response_model=Superheroes)
def get_superheroes():
    return Superheroes(superheroes=memory_db["superheroes"])

@app.post("/superheroes")
def add_superhero(superhero: Superhero):
    memory_db["superheroes"].append(superhero)
    return superhero

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
