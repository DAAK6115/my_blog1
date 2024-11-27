
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from elenizado.models import Cours, Video, Categorie
from django.urls import reverse

@pytest.mark.django_db
def test_cours_creation_and_retrieval(client):
    # Création d'un cours
    cours = Cours.objects.create(
        titre="Test Cours",
        niveau="Débutant",
        annee=2023,
        description="Description test",
        cours=SimpleUploadedFile("test_cours.pdf", b"file_content")
    )
    # Vérification via une vue
    url = reverse('cours')  # Assurez-vous que cette URL existe
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Cours" in response.content.decode()
