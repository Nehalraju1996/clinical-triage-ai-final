import requests
from inference import agent

BASE = "http://127.0.0.1:8001"

def run():
    total = 0
    runs = 5

    for _ in range(runs):
        state = requests.post(f"{BASE}/reset").json()

        done = False
        while not done:
            action = agent(state)
            res = requests.post(f"{BASE}/step", json=action).json()
            state = res["state"]
            reward = res["reward"]
            done = res["done"]

        total += reward

    print("Average Score:", total / runs)

if __name__ == "__main__":
    run()