from qts_api.viewsets import ad_typeViewSet, feedbackViewSet
from qts_api.viewsets import userViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('feedback', feedbackViewSet)
router.register('user', userViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

