import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_should_return_lettings_index(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Lettings' in response.content


@pytest.mark.django_db
def test_should_return_letting_page(client):
    url = reverse('letting', args=[1])
    response = client.get(url)
    assert response.status_code == 200
    assert b'Joshua Tree Green Haus /w Hot Tub' in response.content
