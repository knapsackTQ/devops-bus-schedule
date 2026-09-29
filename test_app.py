from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_routes():
    response = app.test_client().get('/routes')
    assert response.status_code == 200
    assert b"Bus Routes" in response.data

def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data