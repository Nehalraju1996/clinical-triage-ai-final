import requests

url = "https://nehalvysyaraju-clinical-triage-ai-final.hf.space/reset"

res = requests.post(url)

print("Status Code:", res.status_code)
print("Response:", res.json())