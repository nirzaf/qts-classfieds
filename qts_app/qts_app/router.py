from qts_api.viewsets import ad_typeViewSet, promotion_packageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('promotion_package', promotion_packageViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

