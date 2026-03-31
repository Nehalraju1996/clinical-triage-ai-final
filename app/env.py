from typing import Dict
import random

class ClinicalTriageEnv:
    def __init__(self):
        self.step_count = 0

        self.tasks = [
            {
                "symptoms": "Mild fever and cough",
                "severity": "low",
                "test": "none",
                "department": "general",
                "difficulty": "easy"
            },
            {
                "symptoms": "Chest pain and sweating",
                "severity": "high",
                "test": "ecg",
                "department": "cardiology",
                "difficulty": "medium"
            },
            {
                "symptoms": "Severe head injury after accident",
                "severity": "high",
                "test": "ct_scan",
                "department": "neurology",
                "difficulty": "hard"
            }
        ]

    def reset(self) -> Dict:
        self.task = random.choice(self.tasks)
        self.step_count = 0

        self.current_state = {
            "patient_symptoms": self.task["symptoms"],
            "severity": None,
            "test": None,
            "department": None,
            "stage": "severity",
            "difficulty": self.task["difficulty"],
            "done": False
        }

        return self.current_state

    def step(self, action: Dict):
        self.step_count += 1
        reward = 0.0

        if self.current_state["stage"] == "severity":
            self.current_state["severity"] = action.get("severity")
            if self.current_state["severity"] == self.task["severity"]:
                reward += 0.3
            self.current_state["stage"] = "test"

        elif self.current_state["stage"] == "test":
            self.current_state["test"] = action.get("test")
            if self.current_state["test"] == self.task["test"]:
                reward += 0.3
            self.current_state["stage"] = "department"

        elif self.current_state["stage"] == "department":
            self.current_state["department"] = action.get("department")
            if self.current_state["department"] == self.task["department"]:
                reward += 0.4
            self.current_state["done"] = True

        # penalty for inefficiency
        reward -= 0.05 * self.step_count
        reward = max(0.0, min(1.0, reward))

        return self.current_state, reward, self.current_state["done"], {}

    # REQUIRED FOR OPENENV
    def state(self):
        return self.current_state