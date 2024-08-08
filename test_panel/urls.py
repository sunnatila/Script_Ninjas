from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, ScienceViewSet

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'sciences', ScienceViewSet)

urlpatterns = [
    path('create/', include(router.urls)),
]
