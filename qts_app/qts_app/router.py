from qts_api.viewsets import promotion_packageViewSet
from qts_api.viewsets import promoted_ad_detailViewSet
from qts_api.viewsets import feedbackViewSet
from qts_api.viewsets import parent_categoryViewSet
from qts_api.viewsets import sub_categoryViewSet
from qts_api.viewsets import ad_listingViewSet
from qts_api.viewsets import districtViewSet
from qts_api.viewsets import cityViewSet
from qts_api.viewsets import imageViewSet
from qts_api.viewsets import userViewSet
from qts_api.viewsets import ad_typeViewSet
from qts_api.viewsets import paymentViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('ad_type', ad_typeViewSet)
router.register('feedback', feedbackViewSet)
router.register('ad_listing', ad_listingViewSet)
router.register('district', districtViewSet)
router.register('image', imageViewSet)
router.register('promoted_ad_detail', promoted_ad_detailViewSet)
router.register('sub_category', sub_categoryViewSet)
router.register('parent_category', parent_categoryViewSet)
router.register('promotion', promotion_packageViewSet)
router.register('city', cityViewSet)
router.register('user', userViewSet)
router.register('payment', paymentViewSet)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve

