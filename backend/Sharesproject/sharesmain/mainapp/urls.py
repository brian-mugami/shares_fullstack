from django.urls import path, include
from . import views
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("country", views.CountryView.as_view({"post":"create"})),
    path("country/<int:pk>", views.CountryView.as_view({"delete":"destroy"})),
    path('user/register', RegistrationView.as_view(), name='register'),
    path('user/login', LoginView.as_view(), name='login'),
    path('user/logout', LogoutView.as_view(), name='logout'),
    path('user/change-password', ChangePasswordView.as_view(), name='password_change'),
    path('user/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('confirmation/<str:confirmation_id>', views.ConfirmationView.as_view(), name="confirmation"),
    path('reconfirm/<int:id>', views.ConfirmationByUser.as_view(), name="reconfirm")
]