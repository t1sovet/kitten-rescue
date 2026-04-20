from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import AddressViewSet, KittenDetailView, KittenListCreateView, MessageViewSet     
# from api.views import AddressViewSet, AdoptionRequestView, MessageAPIView

urlpatterns = [
    path('api/kittens/', KittenListCreateView.as_view(), name='kitten-list'),
    path('api/kittens/<int:pk>/', KittenDetailView.as_view(), name='kitten-detail'),

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/addresses/', AddressViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='address-list'),
    path('api/messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='message-list'),
    path('admin/', admin.site.urls),
]
