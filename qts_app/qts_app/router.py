from qts_api.viewsets import ad_typeViewSet, ad_listingViewSet
# from qts_app.qts_api.viewsets import ad_typeViewSet, ad_listingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('ad_listing', ad_listingViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

