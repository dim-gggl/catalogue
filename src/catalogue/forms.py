from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import gettext_lazy as _

from .models import *


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['art_type'].widget = forms.Select(
            choices=[(art.name, art.name.upper()) for art in Art.objects.all()]
        )
        self.fields['support'].widget = forms.Select(
            choices=[(sup.name, sup.name.upper()) for sup in Support.objects.all()]
        )
        self.fields['technique'].widget = forms.Select(
            choices=[(tech.name, tech.name.upper()) for tech in Technique.objects.all()]
        )

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = "__all__"

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

class ContextualReferenceForm(forms.ModelForm):
    class Meta:
        model = ContextualReference
        fields = "__all__"

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = "__all__"

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = "__all__"

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "avatar"]
        labels = {
            "username": _("Username"),
            "password": _("Password"),
            "avatar": _("Avatar")
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "bio", "avatar"]
        label = {
            "username": _("Username"),
            "bio": _("Bio"),
            "avatar": _("Avatar")
        }
