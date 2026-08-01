import json
import os

FEEDBACK_FILE = "database/feedback.json"


def save_feedback(data):

    # Create database folder if it doesn't exist
    os.makedirs("database", exist_ok=True)

    feedback = []

    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r") as file:
                feedback = json.load(file)
        except:
            feedback = []

    feedback.append(data)

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(feedback, file, indent=4)