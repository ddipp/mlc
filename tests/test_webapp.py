import pytest

from app import app


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """
    app.config.update({
        "TESTING": True,
    })

    # app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_landing_aliases(client):
    response = client.get("/")
    assert response.data == b'<!doctype html>\n<html lang=en>\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to the target URL: <a href="/mlc/">/mlc/</a>. If not, click the link.\n'
    assert response.request.path == "/"
    assert len(response.history) == 0
