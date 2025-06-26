from django.forms.formsets import BaseFormSet, ManagementForm

from .forms import ArtistForm



class ArtistFormSet(BaseFormSet):

    template_name_div = "catalogue/forms/formsets/div.html"
    template_name_p = "catalogue/forms/formsets/p.html"
    template_name_table = "catalogueforms/formsets/table.html"
    template_name_ul = "catalogue/forms/formsets/ul.html"


    def clean(self):
        super().clean()


