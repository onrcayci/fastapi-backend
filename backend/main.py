from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from typing import List
from numpy import ndarray
from pydantic import BaseModel

from .simulation import music_synthesis

app = FastAPI()

app.mount("/app", StaticFiles(directory="public", html=True), name="public")

class SimulationRequest(BaseModel):
    grid_size: int
    iterations: int
    start_point: List[int]

@app.get("/")
async def root():
    return RedirectResponse(url="/app")

@app.get("/api")
async def api_root():
    return {"message": "Backend developed using FastAPI!"}

@app.get("/api/simulate", response_model=List[List[List[float]]])
async def get_music_simulation():
    result = music_synthesis()
    return result

@app.post("/api/simulate", response_model=List[List[List[float]]])
async def post_music_simulation(simulation_request: SimulationRequest):
    result = music_synthesis(
        grid_size=simulation_request.grid_size,
        iterations=simulation_request.iterations,
        start_point=simulation_request.start_point)
    return result