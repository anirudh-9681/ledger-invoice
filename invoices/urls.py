from rest_framework import routers
from .api import InvoiceViewSet

router = routers.DefaultRouter()
router.register('invoices', InvoiceViewSet, 'invoices')

urlpatterns = router.urls
