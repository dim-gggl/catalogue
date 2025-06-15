from django.contrib import admin

from .models import *


admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Exhibition)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Wishlist)

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_year')

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'art_type', 'support', 'technique')
    list_filter = ('art_type', 'support', 'technique', "artist", )
    search_fields = ('title', 'artist__first_name', 'artist__last_name', 'artist__pseudonym')

@admin.register(ContextualReference)
class ContextualReferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "reference_type", "author", "publication_year")
    list_filter = ("reference_type", "publication_year")
    search_fields = ("name", "author", "publisher", "isbn")
    ordering = ("-publication_year", "name")
