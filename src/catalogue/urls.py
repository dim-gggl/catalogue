from django.urls import path
from django.views.generic import RedirectView

from .views.auth_views import ArtLoginView, ArtLogoutView, SignUpView, HomeListView
from .views.artwork_views import StockListView, ArtworkCreateView
from .views.dashboard_views import DashboardView


urlpatterns = [
    path('', HomeListView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path("login/", ArtLoginView.as_view(), name="login"),
    path("logout/", ArtLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("stock/", StockListView.as_view(), name="stock"),
    path("artworks/add/", ArtworkCreateView.as_view(), name="artwork_add"),
]


