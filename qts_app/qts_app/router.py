from qts_api.viewsets import ad_typeViewSet, feedbackViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('feedback', feedbackViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

