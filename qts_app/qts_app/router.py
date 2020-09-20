from qts_api.viewsets import ad_typeViewSet, promotion_packageViewSet,  feedbackViewSet, sub_categoryViewSet
from qts_api.viewsets import ad_listingViewSet
from qts_api.viewsets import districtViewSet
from qts_api.viewsets import ad_typeViewSet, feedbackViewSet
from qts_api.viewsets import userViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('feedback', feedbackViewSet)
router.register('ad_listing', ad_listingViewSet)
router.register('district', districtViewSet)
router.register('sub_category', sub_categoryViewSet)
router.register('user', userViewSet)


# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

