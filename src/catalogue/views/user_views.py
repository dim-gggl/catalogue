from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.utils.translation import gettext_lazy as _
from django.conf.settings import AUTH_USER_MODEL
from django.urls import reverse_lazy

from ..models.user import User
from ..forms import UserForm


class UserListView(LoginRequiredMixin, ListView):
    model = AUTH_USER_MODEL
    template_name = 'catalogue/user_list.html'
    context_object_name = 'users'
    login_url = 'login'
    paginate_by = 20


class UserDetailView(LoginRequiredMixin, DetailView):
    model = AUTH_USER_MODEL
    template_name = 'catalogue/user_detail.html'
    context_object_name = 'user'
    login_url = 'login'
    pk_url_kwarg = 'user_id'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = AUTH_USER_MODEL
    template_name = 'catalogue/user_form.html'
    fields = ['username', 'email', 'bio', 'avatar']
    login_url = 'login'
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_id': self.object.pk})


class UserCreateView(CreateView):
    model = AUTH_USER_MODEL
    template_name = "catalogue/user_form.html"
    fields = ["username", "password", "avatar"]
    form_class = UserForm
