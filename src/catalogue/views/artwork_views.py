from django.views.generic import DetailView, CreateView, ListView

from ..models.artwork import Artwork
from ..forms import ArtworkForm


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "catalogue/artwork_detail.html"

    def get_queryset(self):
        return Artwork.objects.all()


class StockListView(ListView):
    """Displays a paginated list of artworks available in stock."""

    model = Artwork
    template_name = "catalogue/stock_list.html"
    paginate_by = 20


class ArtworkCreateView(CreateView):
    """Form view used to create a new ``Artwork`` instance."""

    model = Artwork
    form_class = ArtworkForm
    template_name = "catalogue/artwork_form.html"