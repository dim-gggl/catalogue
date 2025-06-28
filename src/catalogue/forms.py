from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import (
    Artwork,
    Art,
    Artist,
    Collection,
    Comment,
    ContextualReference,
    Exhibition,
    Location,
    Support,
    Tag,
    Technique,
    Wishlist,
    User,
)


class CatalogueUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__"


class CatalogueUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "email", "bio", "profile_picture"]


class ArtForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['art_type'].widget = forms.Select(
    #         choices=[(art.name, art.name.upper()) for art in Art.objects.all()]
    #     )
    #     self.fields['support'].widget = forms.Select(
    #         choices=[(sup.name, sup.name.upper()) for sup in Support.objects.all()]
    #     )
    #     self.fields['technique'].widget = forms.Select(
    #         choices=[(tech.name, tech.name.upper()) for tech in Technique.objects.all()]
    #     )

class ArtworkForm(forms.ModelForm):

    # Champs pour créer de nouveaux objets
    new_art_type = forms.CharField(
        max_length=100, 
        required=False, 
        label=_("Nouveau type d'art"),
        help_text=_("Laissez vide si vous sélectionnez un type existant"),
        widget=forms.TextInput(attrs={'placeholder': 'Nom du nouveau type d\'art'})
    )
    new_support = forms.CharField(
        max_length=100, 
        required=False, 
        label=_("Nouveau support"),
        help_text=_("Laissez vide si vous sélectionnez un support existant"),
        widget=forms.TextInput(attrs={'placeholder': 'Nom du nouveau support'})
    )
    new_technique = forms.CharField(
        max_length=100, 
        required=False, 
        label=_("Nouvelle technique"),
        help_text=_("Laissez vide si vous sélectionnez une technique existante"),
        widget=forms.TextInput(attrs={'placeholder': 'Nom de la nouvelle technique'})
    )
    new_artist = forms.CharField(
        max_length=100,
        required=False,
        label=_("Nouvel artiste"),
        help_text=_("Laissez vide si vous sélectionnez un artiste existant"),
        widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'artiste'})
    )

    class Meta:
        model = Artwork
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": _("Titre de l'oeuvre")}),
            "description": forms.Textarea(attrs={"placeholder": _("Cours texte descriptif")}),
            "image": forms.FileInput(attrs={"placeholder": _("Image de l'oeuvre")}),
            "collection": forms.Select(attrs={"placeholder": _("Collection")}),
            "notes": forms.Textarea(attrs={"placeholder": _("Notes")}),
            "tags": forms.SelectMultiple(attrs={"placeholder": _("Mots clés pour référencement")}),
        }
        labels = {
            "title": _("Titre"),
            "description": _("Description"),
            "image": _("Image"),
            "artist": _("Artiste"),
            "collection": _("Collection"),
            "art_type": _("Type d'art"),
            "support": _("Support"),
            "technique": _("Technique"),
            "creation_year": _("Année"),
            "width_cm": _("Largeur (cm)"),
            "height_cm": _("Hauteur (cm)"),
            "depth_cm": _("Profondeur (cm)"),
            "weight_kg": _("Poids (kg)"),
            "acquisition_date": _("Date d'Acquisition"),
            "acquisition_place": _("Lieu d'Acquisition"),
            "price_eur": _("Prix (€)"),
            "provenance": _("Provenance"),
            "notes": _("Notes"),
            "is_framed": _("Est encadré"),
            "is_on_loan": _("Est prêté"),
            "collections": _("Collections"),
            "tags": _("Étiquettes"),
            "exhibitions": _("Expositions"),
            "location": _("Lieu"),
            "is_signated": _("est signé"),
            "contextual_references": _("Références contextuelles"),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        # Gestion du type d'art
        art_type = cleaned_data.get('art_type')
        new_art_type = cleaned_data.get('new_art_type')
        
        if not art_type and new_art_type:
            # Créer un nouveau type d'art
            art_type, created = Art.objects.get_or_create(name=new_art_type.strip())
            cleaned_data['art_type'] = art_type
        elif not art_type and not new_art_type:
            raise forms.ValidationError(
                _(
                    "Vous devez soit sélectionner un type d'art "
                    "existant, soit en créer un nouveau."
                )
            )
        
        # Gestion du support
        support = cleaned_data.get('support')
        new_support = cleaned_data.get('new_support')
        
        if not support and new_support:
            # Créer un nouveau support
            support, created = Support.objects.get_or_create(
                name=new_support.strip()
            )
            cleaned_data['support'] = support
        elif not support and not new_support:
            raise forms.ValidationError(
                _(
                    "Vous devez soit sélectionner un support existant, "
                    "soit en créer un nouveau."
                )
            )
        
        # Gestion de la technique
        technique = cleaned_data.get('technique')
        new_technique = cleaned_data.get('new_technique')
        
        if not technique and new_technique:
            # Créer une nouvelle technique
            technique, created = Technique.objects.get_or_create(
                name=new_technique.strip()
            )
            cleaned_data['technique'] = technique
        elif not technique and not new_technique:
            raise forms.ValidationError(
                _(
                    "Vous devez soit sélectionner une technique "
                    "existante, soit en créer une nouvelle."
                )
            )
        
        artist = cleaned_data.get('artist')
        new_artist = cleaned_data.get('new_artist')
        
        if not artist and new_artist:
            # Créer un nouvel artiste
            artist, created = Artist.objects.get_or_create(
                pseudonym=new_artist.strip()
            )
            cleaned_data['artist'] = artist
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Les objets ont déjà été créés dans clean()
        if commit:
            instance.save()
            self.save_m2m()
        
        return instance


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = "__all__"

class Comment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content", "artwork", "user"]
        labels = {
            "content": _("Contenu"),
            "artwork": _("Œuvre"),
            "user": _("Utilisateur"),
        }

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
        fields = ["name", "description"]
        labels = {
            "name": _("Nom"),
            "description": _("Description"),
        }

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ["name"]

class TechniqueForm(forms.ModelForm):

    class Meta:
        model = Technique
        fields = ["name", "description"]
        labels = {
            "name": _("Nom"),
            "description": _("Description"),
        }

class WishlistForm(forms.ModelForm):

    class Meta:
        model = Wishlist
        fields = "__all__"

