from fastapi import FastAPI
from app.env import ClinicalTriageEnv
from pydantic import BaseModel

app = FastAPI()

env = ClinicalTriageEnv()

class ActionRequest(BaseModel):
    action: str

@app.get("/")
def root():
    return {"message": "Clinical Triage AI Running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs,
        "info": {"message": "reset successful"}
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