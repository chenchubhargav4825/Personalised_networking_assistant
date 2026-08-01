def extract_event_themes(description):
    description = description.lower()

    topics = []

    if "ai" in description or "artificial intelligence" in description:
        topics.append("Artificial Intelligence")

    if "machine learning" in description:
        topics.append("Machine Learning")

    if "blockchain" in description:
        topics.append("Blockchain")

    if "cloud" in description:
        topics.append("Cloud Computing")

    if "cyber" in description:
        topics.append("Cyber Security")

    if "data" in description:
        topics.append("Data Science")

    if "web" in description:
        topics.append("Web Development")

    if len(topics) == 0:
        topics = [
            "Networking",
            "Technology",
            "Innovation"
        ]

    return topics[:3]