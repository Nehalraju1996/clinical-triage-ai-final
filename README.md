---
title: Clinical Triage AI
emoji: "🧠"
colorFrom: blue
colorTo: green
sdk: docker
app_file: app/api.py
pinned: false
---

# 🏆 Clinical Triage AI – OpenEnv Environment

## 📌 Overview
This project simulates a real-world hospital triage system where an AI agent must:
1. Assign severity
2. Recommend diagnostic test
3. Route to correct department

## 🧠 Features
- Multi-step decision environment
- 3 difficulty levels (easy → medium → hard)
- Deterministic grading (0.0–1.0)
- Reward shaping (partial + final reward)
- OpenEnv compliant (reset, step, state)

## 📊 Tasks
| Symptoms | Severity | Test | Department |
|----------|--------|------|-----------|
| Fever | Low | None | General |
| Chest Pain | High | ECG | Cardiology |
| Head Injury | High | CT Scan | Neurology |

## ⚙️ Run Locally