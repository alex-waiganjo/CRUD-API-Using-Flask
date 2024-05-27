import json

def test_post_route(test_client):    
    payload = {
        "username": "Lopez",
        "age": 35,
        "email": "Lopez33@gmail.com",
        "residence": "Thindigua"
    }
    response = test_client.post('/information', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['username'] == "Lopez"
    assert data['age'] == 35
    assert data['email'] == "Lopez33@gmail.com"
    assert data['residence'] == "Thindigua"


def test_get_routes(test_client):
    response = test_client.get('/information')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0

def test_get_route(test_client):
    response = test_client.get('/information/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["username"] == "Lopez"
    assert data['age'] == 35
    assert data['email'] == "Lopez33@gmail.com"
    assert data['residence'] == "Thindigua"

def test_update_route(test_client):
    payload = {
        "username": "Jane",
        "age": 35,
        "email": "jane33@gmail.com",
        "residence": "Thika"
    }
    response = test_client.put('/information/1', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['username'] == "Jane"
    assert data['age'] == 35
    assert data['email'] == "jane33@gmail.com"
    assert data['residence'] == "Thika"

def test_delete_route(test_client):
    response = test_client.delete('/information/1')
    assert response.status_code == 200
