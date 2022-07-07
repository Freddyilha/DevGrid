import requests

def test_app_home_should_return_Hello_World():
    url = "http://host.docker.internal:5001"

    response = requests.get(url)

    assert response.status_code == 200

