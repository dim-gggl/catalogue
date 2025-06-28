from django.urls import path
from django.views.generic import RedirectView

from .views.auth_views import ArtLoginView, ArtLogoutView, SignUpView, HomeListView
from .views.artwork_views import StockListView, ArtworkCreateView, ArtworkDetailView, ExposedArtworksView
from .views.dashboard_views import DashboardView
from .views.user_views import WishlistView, WishlistAddView, WishlistRemoveView


urlpatterns = [
    path('', HomeListView.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path("login/", ArtLoginView.as_view(), name="login"),
    path("logout/", ArtLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("stock/", StockListView.as_view(), name="stock"),
    path("artworks/add/", ArtworkCreateView.as_view(), name="artwork_add"),
    path("artworks/<int:pk>/", ArtworkDetailView.as_view(), name="artwork_display"),
    path("artworks/exposed/", ExposedArtworksView.as_view(), name="exposed_artworks"),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/add/<int:artwork_id>/', WishlistAddView.as_view(), name='wishlist_add'),
    path('wishlist/remove/<int:artwork_id>/', WishlistRemoveView.as_view(), name='wishlist_remove'),
]


