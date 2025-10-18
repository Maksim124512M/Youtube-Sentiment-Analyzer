import pytest

from fastapi.testclient import TestClient

from endpoint import app

client = TestClient(app)

def test_home():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to sentiment analyzer'}


def test_analyze_video():
    # Using a sample video ID for testing
    video_id = 'dQw4w9WgXcQ'  # Rick Astley - Never Gonna Give You Up

    response = client.get(f'/analyze/{video_id}/')

    assert response.status_code == 200
    assert response.headers['content-type'] == 'image/png'