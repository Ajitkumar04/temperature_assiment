import json
data = {
    "game": "Adventure Quest",
    "level": 15,
    "score": 8500,
    "inventory": ["sword", "shield", "potion"]
}

with open("gave_data.json", "w") as f:
  json.dump(data, f, indent=2)
