import pytest
from elenizado.models import Publication, Commentaire, Categorie
from django.urls import reverse

@pytest.mark.django_db
def test_publication_comment_flow(client):
    categorie = Categorie.objects.create(nom="Tech", description="Tech news")
    publication = Publication.objects.create(
        titre="Nouvelle technologie",
        description="Description des nouvelles technologies",
        categorie=categorie
    )

    # Soumission de commentaire
    url = reverse('is_commentaire')
    data = {
        "publication_id": publication.id,
        "nom": "John Doe",
        "email": "john@example.com",
        "commentaire": "Très intéressant !"
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Commentaire.objects.filter(publication=publication).count() == 1
