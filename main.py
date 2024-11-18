from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Figure(BaseModel):
    name: str 
    manufacture: Optional[str]
    line: str
    collection: str


@app.get("/")
async def root():
    return "root"

@app.get("/api/v1/figures/{figure_id}")
def get_figure(figure_id: int):
    figure = {"id": figure_id, "name": "Chun-Li - Outfit 2", "Manufacture": "Tamashii Nation", "Line": "SH Figuarts", "Collection": "Street Fighter"}
    return {"figure": figure}

@app.post("/api/v1/figures")
def create_figure(figure: Figure):
    return {"status": "Figure added"}

