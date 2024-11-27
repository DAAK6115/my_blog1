import pytest
from website.models import SiteInfo

@pytest.mark.django_db
def test_siteinfo_status_toggle():
    site_info = SiteInfo.objects.create(
        nom="Test Site",
        email="test@example.com",
        telephone="123456789"
    )
    site_info.status = False
    site_info.save()
    assert site_info.status is False