import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_flow(client, create_test_user):
    # Crée un utilisateur administrateur
    create_test_user

    # Simuler des données de connexion
    login_data = {"username": "testuser", "password": "ValidPass123!"}

    # URL de connexion admin
    login_url = reverse('admin:login')

    # Poster les données de connexion
    response = client.post(login_url, login_data)

    # Afficher le contenu de la réponse en cas d'échec
    if response.status_code != 302:
        print(response.content.decode())

    # Vérifier que la connexion a réussi
    assert response.status_code == 302
