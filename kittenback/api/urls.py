from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KittenViewSet, MessageViewSet, AddressViewSet, RegisterView, AdoptionRequestViewSet

router = DefaultRouter()
router.register(r'kittens', KittenViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'adoption-requests', AdoptionRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api/', include(router.urls))
]