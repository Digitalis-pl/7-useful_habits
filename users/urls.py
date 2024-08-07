from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.UserCreateAPI.as_view(), name='user-create'),
    path('<int:pk>/', views.UserViewAPI.as_view(), name='user'),
    path('all/', views.UserListViewAPI.as_view(), name='all-users'),
    path('<int:pk>/update/', views.UserUpdateAPI.as_view(), name='user-update'),
    path('<int:pk>/delete', views.UserDeleteAPI.as_view(), name='user-delete'),
]
