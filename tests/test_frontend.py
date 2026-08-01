from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_home_page_serves_html():
    response = client.get("/")
    assert response.status_code == 200
    assert "Personalized Networking Assistant" in response.text


def test_analyze_endpoint_returns_topics():
    response = client.post(
        "/analyze",
        json={"description": "Join our AI and machine learning meetup", "interests": ["AI", "startups"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "topics" in data
    assert len(data["topics"]) > 0
