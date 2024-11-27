import pytest
from website.models import SiteInfo

@pytest.mark.django_db
def test_siteinfo_creation():
    site_info = SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone="123456789"
    )
    assert site_info.nom == "Test Site"
    assert site_info.email == "test@example.com"
    assert site_info.status is True
    