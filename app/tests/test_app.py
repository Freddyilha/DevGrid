import requests
import responses

def test_app_home_should_return_Hello_World():
    url = "http://localhost:5001"
    rsp1 = responses.Response(
        method="GET",
        url="http://localhost:5001",
    )
    responses.add(rsp1)

    a = requests.get("http://localhost:5001")

    print(a)
