from fastapi import FastAPI
from typing import List
from numpy import ndarray
from pydantic import BaseModel

from simulation import music_synthesis

app = FastAPI()

class SimulationRequest(BaseModel):
    grid_size: int
    iterations: int
    start_point: List[int]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/simulate", response_model=List[List[List[float]]])
async def music_simulation():
    result = music_synthesis()
    return result

@app.post("/simulate", response_model=List[List[List[float]]])
async def music_simulation(simulation_request: SimulationRequest):
    result = music_synthesis(
        grid_size=simulation_request.grid_size,
        iterations=simulation_request.iterations,
        start_point=simulation_request.start_point)
    return result