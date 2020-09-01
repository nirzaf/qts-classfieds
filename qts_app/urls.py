from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qts_api.urls')),
    path('', admin.site.urls)
]
