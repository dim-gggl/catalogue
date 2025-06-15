from django.views.generic import DetailView, CreateView
from ..models.artwork import Artwork


class ArtworkDetailView(DetailView):
    model = Artwork

    def get_queryset(self, request, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

