from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KittenViewSet, MessageViewSet, AddressViewSet, RegisterView

router = DefaultRouter()
router.register(r'kittens', KittenViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
]