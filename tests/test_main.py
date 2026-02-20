import pytest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_calculate(client):
    response = client.post('/api/calculate',
        json={'expression': '10+5'})
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['result'] == 15
