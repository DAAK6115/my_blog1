import pytest
from django.urls import reverse
from website.models import SiteInfo

@pytest.mark.django_db
def test_about_view(client):
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200
    assert "À propos" in response.content.decode()
