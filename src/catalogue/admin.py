from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User
# from .forms import CatalogueUserCreationForm, CatalogueUserChangeForm

from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(User)
class CatalogueUserAdmin(UserAdmin):
    # add_form = CatalogueUserCreationForm
    # form = CatalogueUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active")
    list_filter  = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("birth_date",)}),
        ("Permissions", {"fields": ("is_staff","is_active","is_superuser","groups")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email","password1","password2","is_staff","is_active")
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Exhibition)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Wishlist)

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = (_('name'),)

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = (_('name'),)

@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = (_('name'),)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (_('last_name'), _('first_name'), _('birth_year'))

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = (_('title'), _('artist'), _('art_type'), _('support'), _('technique'))
    list_filter = (_('art_type'), _('support'), _('technique'), _('artist'), )
    search_fields = (_('title'), _('artist__first_name'), _('artist__last_name'), _('artist__pseudonym'))

@admin.register(ContextualReference)
class ContextualReferenceAdmin(admin.ModelAdmin):
    list_display = (_("name"), _("reference_type"), _("author"), _("publication_year"))
    list_filter = (_("reference_type"), _("publication_year"))
    search_fields = (_("name"), _("author"), _("publisher"), _("isbn"))
    ordering = (_("-publication_year"), _("name"))
()