from django.urls import path
from django.views.generic import RedirectView

from .views.auth_views import ArtLoginView, ArtLogoutView, SignUpView, HomeListView


urlpatterns = [
    path('', HomeListView.as_view(), name='homepage'),
    path("login/", ArtLoginView.as_view(), name="login"),
    path("logout/", ArtLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]


