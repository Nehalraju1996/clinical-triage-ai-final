from fastapi import FastAPI
from pydantic import BaseModel
from app.env import ClinicalTriageEnv

app = FastAPI()
env = ClinicalTriageEnv()

class Action(BaseModel):
    severity: str = None
    test: str = None
    department: str = None

@app.get("/")
def root():
    return {"message": "Clinical Triage API Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action.dict())
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }