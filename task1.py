import json
def task() -> float:
    jsonf = 'input.json'
    with open(jsonf, 'r') as f:
        json_data = json. load (f)
    totals = sum ([item["score"] * item["weight"] for item in json_data])
    return round (totals,3)

print (task())
