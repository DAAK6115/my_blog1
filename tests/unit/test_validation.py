import pytest
from django.core.exceptions import ValidationError
from elenizado.models import Cours, Video, Categorie
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
class TestModelFieldValidations:
    def test_validation(self):
        # Test avec une année négative
        with pytest.raises(ValidationError):
            cours = Cours(
                titre="Test Cours Invalide",
                niveau="Débutant",
                annee=-1,  # Année invalide
                description="Description test",
                cours=SimpleUploadedFile("test_cours.pdf", b"file_content")
            )
            cours.full_clean()

    def test_video_url_validation(self):
        # Test avec une URL invalide
        with pytest.raises(ValidationError):
            video = Video(
                titre="Test Video",
                description="Description test",
                video="invalid_url",
                image=SimpleUploadedFile("test_image.jpg", b"file_content")
            )
            video.full_clean()