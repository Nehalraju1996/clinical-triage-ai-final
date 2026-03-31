from fastapi import FastAPI
from pydantic import BaseModel
from app.env import ClinicalTriageEnv

app = FastAPI()

env = ClinicalTriageEnv()

class ActionRequest(BaseModel):
    action: str

@app.get("/")
def root():
    return {"message": "Clinical Triage AI API Running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs,
        "info": {"message": "Environment reset successful"}
    }

@app.post("/step")
def step(req: ActionRequest):
    obs, reward, done, info = env.step(req.action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }