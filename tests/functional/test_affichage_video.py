import pytest
from django.urls import reverse
from website.models import SiteInfo

@pytest.mark.django_db
def test_get_video(client):
    # Simule l'accès à une vue vidéo
    url = reverse('video')  # Assurez-vous que cette URL existe dans votre projet
    response = client.get(url)
    assert response.status_code == 200
    assert "Vidéo" in response.content.decode()