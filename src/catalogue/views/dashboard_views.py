from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ..models.artwork import Artwork, Artist


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "catalogue/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "exhibited_artworks": Artwork.objects.filter(
                exhibitions__isnull=False
            ).distinct(),
            "loaned_artworks": Artwork.objects.filter(is_on_loan=True),
            "random_artworks": Artwork.objects.order_by('?')[:3],
            "artists": Artist.objects.all(),
        })
        return context

    # def post_wishlist(self, request, *args, **kwargs):
        
