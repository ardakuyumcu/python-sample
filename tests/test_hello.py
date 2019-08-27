import pytest

from hello import hello


@pytest.fixture
def client():
    hello.app.config['TESTING'] = True

    with hello.app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/hello')
    assert b'Hello, World!' in response.data
