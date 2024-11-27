import pytest
from django.core.exceptions import ValidationError
from elenizado.models import Cours, Video, Categorie
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
class TestModelConstraints:
    def test_unique_constraints(self):
        categorie = Categorie.objects.create(nom="Test Categorie", description="Description test")
        assert Categorie.objects.filter(nom="Test Categorie").count() == 1