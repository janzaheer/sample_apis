from django.urls import path, include
from rest_framework.routers import DefaultRouter
from edxapp.views import GreetingViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'api/v1/greetings', GreetingViewSet, basename='greeting')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]