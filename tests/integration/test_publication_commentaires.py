import pytest
from elenizado.models import Publication, Commentaire, Categorie

@pytest.mark.django_db
def test_publication_with_commentaires():
    # Crée une catégorie
    categorie = Categorie.objects.create(nom="Tech", description="Description Tech")
    # Crée une publication associée
    publication = Publication.objects.create(
        titre="Test Publication",
        description="Description",
        slug="test-publication",
        categorie=categorie
    )
    # Ajoute des commentaires à la publication (en passant l'instance directement)
    Commentaire.objects.create(
        publication=publication,  # Passe l'instance, pas l'ID
        nom="John Doe",
        email="john@example.com",
        commentaire="Super post !"
    )
    Commentaire.objects.create(
        publication=publication,  # Passe l'instance, pas l'ID
        nom="Jane Doe",
        email="jane@example.com",
        commentaire="Très intéressant !"
    )
    # Vérifie que la relation est correcte
    assert hasattr(publication, 'publication_commentaire')  # Vérifie que l'attribut existe
    assert publication.publication_commentaire.count() == 2  # Vérifie le nombre de commentaires
