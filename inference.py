def agent(state):
    symptoms = state["patient_symptoms"].lower()
    stage = state["stage"]

    if stage == "severity":
        if "chest" in symptoms or "injury" in symptoms:
            return {"severity": "high"}
        return {"severity": "low"}

    if stage == "test":
        if "chest" in symptoms:
            return {"test": "ecg"}
        if "head" in symptoms:
            return {"test": "ct_scan"}
        return {"test": "none"}

    if stage == "department":
        if "chest" in symptoms:
            return {"department": "cardiology"}
        if "head" in symptoms:
            return {"department": "neurology"}
        return {"department": "general"}