import pytest
from website.models import SiteInfo, SocialCount

@pytest.mark.django_db
def test_create_siteinfo():
    site = SiteInfo.objects.create(
        email="info@example.com",
        nom="Mon Site",
        telephone=123456789,
        description="Description du site",
        logo="logo.jpg"
    )
    assert site.email == "info@example.com"
    assert site.nom == "Mon Site"

@pytest.mark.django_db
def test_create_social_count():
    social = SocialCount.objects.create(
        nom="Facebook",
        lien="https://facebook.com",
        icones="fa-facebook-f"
    )
    assert social.nom == "Facebook"
    assert social.lien == "https://facebook.com"
    assert social.icones == "fa-facebook-f"
