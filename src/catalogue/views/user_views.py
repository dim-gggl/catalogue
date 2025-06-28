from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse_lazy

from ..models.user import User
from ..models.artwork import Artwork
from ..models.wishlist import Wishlist
from ..forms import CatalogueUserChangeForm as UserForm, WishlistForm


class UserListView(LoginRequiredMixin, ListView):
    model = settings.AUTH_USER_MODEL
    template_name = 'catalogue/user_list.html'
    context_object_name = 'users'
    login_url = 'login'
    paginate_by = 20


class UserDetailView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'catalogue/user_detail.html'
    context_object_name = 'user'
    login_url = 'login'
    pk_url_kwarg = 'user_id'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = settings.AUTH_USER_MODEL
    template_name = 'catalogue/user_form.html'
    fields = ['username', 'email', 'bio', 'avatar']
    login_url = 'login'
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_id': self.object.pk})


class UserCreateView(CreateView):
    model = settings.AUTH_USER_MODEL
    template_name = "catalogue/user_form.html"
    fields = ["username", "password", "avatar"]
    form_class = UserForm


class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'catalogue/wishlist_detail.html'
    context_object_name = 'wishlist'
    login_url = 'login'

    def get_queryset(self):
        return Wishlist.objects.get_or_create(user=self.request.user)[0]


class WishlistAddView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        artwork_id = kwargs.get('artwork_id')
        artwork = get_object_or_404(Artwork, id=artwork_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.add_artwork(artwork)
        return redirect('wishlist_detail')


class WishlistRemoveView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        artwork_id = kwargs.get('artwork_id')
        artwork = get_object_or_404(Artwork, id=artwork_id)
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.remove_artwork(artwork)
        return redirect('wishlist_detail')
