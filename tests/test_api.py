import requests

def test_api():
    url = "http://localhost:8000/predict"
    data = {"text": "I hate life"}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "enfermedad" in response.json()
    print("Prueba exitosa:", response.json())

if __name__ == "__main__":
    test_api()
