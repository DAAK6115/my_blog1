import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_contact_view(client):
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200
    assert "Contactez-nous" in response.content.decode()