import pytest
from oeuvre.models import Poesie

@pytest.mark.django_db
def test_poeme_creation():
    poeme = Poeme.objects.create(
        titre="Test Poeme",
        contenu="Voici un contenu de test.",
        auteur="Test Auteur"
    )
    assert poeme.titre == "Test Poeme"
    assert poeme.contenu == "Voici un contenu de test."
    assert poeme.auteur == "Test Auteur"
    assert poeme.status is True