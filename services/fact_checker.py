import requests

def verify_fact(topic):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        print(response.text)   # <-- Debug

        if response.status_code == 200:

            data = response.json()

            return {
                "status": "Verified",
                "summary": data.get("extract", "No summary available.")
            }

        return {
            "status": "Not Found",
            "summary": "No information found."
        }

    except Exception as e:
        return {
            "status": "Error",
            "summary": str(e)
        }