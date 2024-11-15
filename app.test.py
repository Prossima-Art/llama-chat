from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_chat_valid_response():
    model = "llama2"
    messages = "Hello, how are you?"
    response = client.get(f"/chat?model={model}&messages={messages}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "message" in response.json()
    assert "content" in response.json()["message"]
    assert isinstance(response.json()["message"]["content"], str)
    assert len(response.json()["message"]["content"]) > 0


def test_generate_valid_response():
    model = "llama2"
    prompt = "Tell me a joke"
    response = client.get(f"/generate?model={model}&prompt={prompt}")
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)
    assert len(response.json()["response"]) > 0


def test_generate_invalid_model():
    model = "invalid_model"
    prompt = "Tell me a joke"
    response = client.get(f"/generate?model={model}&prompt={prompt}")
    assert response.status_code == 422
    assert "detail" in response.json()
    assert "Model 'invalid_model' not found" in response.json()[
        "detail"][0]["msg"]
