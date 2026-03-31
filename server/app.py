from fastapi import FastAPI
from app.env import ClinicalTriageEnv
from pydantic import BaseModel
import uvicorn

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

# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ REQUIRED ENTRYPOINT
if __name__ == "__main__":
    main()