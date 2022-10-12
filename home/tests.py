import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_should_return_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Welcome to Holiday Homes' in response.content
