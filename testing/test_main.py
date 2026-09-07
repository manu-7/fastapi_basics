from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test home api

def test_home():
    response = client.get("/")
    
    #status_code check
    assert response.status_code == 200
    
    #Response data check
    assert response.json() == {"message":"Hello manu"}
    
# test add api

def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result":8}