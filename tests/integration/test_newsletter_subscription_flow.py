import pytest
from django.urls import reverse
from website.models import Newsletter, SiteInfo

@pytest.mark.django_db
def test_newsletter_subscription_flow(client):
    # Créer une instance de SiteInfo
    SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone="123456789"
    )
    
    # Tester l'abonnement à la newsletter
    url = reverse('is_newsletter')
    data = {"email": "subscriber@example.com"}
    response = client.post(url, data)
    
    assert response.status_code == 200
    assert Newsletter.objects.filter(email="subscriber@example.com").exists()
