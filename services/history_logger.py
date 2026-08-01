import json
import os

HISTORY_FILE = "database/history.json"


def save_history(data):

    # Create database folder if it doesn't exist
    os.makedirs("database", exist_ok=True)

    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
        except:
            history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)