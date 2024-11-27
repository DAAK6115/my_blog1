import pytest
from oeuvre.models import Poesie

@pytest.mark.django_db
def test_poeme_status_toggle():
    poeme = Poeme.objects.create(
        titre="Test Poeme",
        contenu="Voici un contenu de test.",
        auteur="Test Auteur"
    )
    poeme.status = False
    poeme.save()
    assert poeme.status is False