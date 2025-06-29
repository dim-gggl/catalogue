from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from ..models.artwork import Artwork, Artist
from ..models.wishlist import Wishlist
from ..forms import ArtworkForm


class ArtworkDetailView(DetailView):

    model = Artwork
    form_class = ArtworkForm
    template_name = "catalogue/artwork_display.html"

    def get_queryset(self):
        return Artwork.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
            context['artwork_in_wishlist'] = wishlist.is_in_wishlist(self.object)
        else:
            context['artwork_in_wishlist'] = False
        return context


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
    success_url = reverse_lazy('artwork_display')

    def get_success_url(self):
        return reverse("artwork_display", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = Artist.objects.all()
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
        valid_artists = form.cleaned_data.get("artists")
        for artist in valid_artists:
            artist.save()
        form.instance.owner = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["artist"].queryset = Artist.objects.all()
        return form


class ExposedArtworksView(ListView):
    """Displays artworks currently part of an active exhibition."""
    model = Artwork
    template_name = "catalogue/exposed_artworks.html"
    context_object_name = "artworks"
    paginate_by = 20

    def get_queryset(self):
        today = timezone.now().date()
        return Artwork.objects.filter(
            exhibitions__start_date__lte=today,
            exhibitions__end_date__gte=today
        ).distinct().order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _("Exposed Artworks")
        return context
