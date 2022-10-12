import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_should_return_profiles_index(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Profiles' in response.content


@pytest.mark.django_db
def test_should_return_profile_page(client):
    url = reverse('profile', args=['HeadlinesGazer'])
    response = client.get(url)
    assert response.status_code == 200
    assert b'HeadlinesGazer' in response.content
