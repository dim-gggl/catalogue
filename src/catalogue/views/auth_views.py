from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from .. import models

from ..forms import SignUpForm


class ArtLoginView(LoginView):
    template_name = "catalogue/login.html"

class ArtLogoutView(LogoutView):
    template_name = "catalogue/logout.html"

    def get(self):
        return redirect("login")


class SignUpView(View):
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class
        return render(
            request=request,
            template_name="catalogue/signup.html",
            context={"form": form}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        button_text = "Inscription"

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(
            request=request,
            template_name="catalogue/signup.html",
            context={
                "form": form,
                }
            )


class HomeListView(LoginRequiredMixin, ListView):
    template_name = "catalogue/home.html"

    def get_queryset(self):
        return models.Artwork.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                "queryset": self.get_queryset()
            }
            return render(request, self.template_name, context=context)
        else:
            return redirect("catalogue/login.html")





