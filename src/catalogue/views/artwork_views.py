from django.views.generic import DetailView, CreateView, ListView

from ..models.artwork import Artwork, Artist
from ..forms import ArtworkForm


class ArtworkDetailView(DetailView):

    model = Artwork
    template_name = "catalogue/artwork_display.html"

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
    redirect_template = "catalogue/artwork_display.html"

    def get_success_url(self):
        return reverse("artwork_display", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artist"] = Artist.objects.all()
        return context
    
    def get_template_names(self):
        if self.request.method == "POST":
            return [self.redirect_template]
        return [self.template_name]

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        valid_artists = form.cleaned_data.get("artists_pseudonyms")
        for artist in valid_artists:
            artist.save()
        form.save()
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["artist"].queryset = Artist.objects.all()
        return form
    
