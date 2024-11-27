import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_is_commentaire_view(client):
    url = reverse('is_commentaire')  # Assurez-vous que cette URL existe
    response = client.post(url, {
        "publication_id": 1,
        "nom": "John Doe",
        "email": "john@example.com",
        "commentaire": "Super post !"
    })
    assert response.status_code == 200  # Vérifiez les statuts attendus