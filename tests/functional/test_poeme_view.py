import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_poeme_view(client):
    url = reverse('poeme')
    response = client.get(url)
    assert response.status_code == 200
    assert "Liste des poèmes" in response.content.decode()
