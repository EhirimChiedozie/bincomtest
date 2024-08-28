from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Lga, AnnouncedPuResults
from .forms import PollingUnitResultsForm, LgaForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your views here.

def home(request):
    return render(request, 'elections/home.html')

class LgaListView(ListView):
    model = Lga
    template_name = 'elections/lgas.html'
    context_object_name = 'lga_dict'

    def get_queryset(self):
        lgas = Lga.objects.all()
        lga_ids = [lga.lga_id for lga in lgas]
        lga_names = [lga.lga_name for lga in lgas]
        lga_dict = {}
        for i in range(len(lga_ids)):
            lga_dict[lga_ids[i]] = lga_names[i]
        return lga_dict
    

def polling_unit_results(request):
    if request.method == 'POST':
        form = PollingUnitResultsForm(request.POST)
        if form.is_valid():
            pu_id = form.cleaned_data.get('polling_unit_uniqueid')
            polling_units = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pu_id).all()
            
            context = {'polling_units':polling_units}
            return render(request, 'elections/polling_unit_results.html', context=context)
    else:
        form = PollingUnitResultsForm()
    context = {
        'form':form
    }
    return render(request, 'elections/pu_results_form.html', context=context)

def lga_form(request):
    if request.method == 'POST':
        form = LgaForm(request.POST)
        if form.is_valid():
            lga_id = form.cleaned_data.get('lga_id')
    return render('elections/lga_form.html')

def polling_units_results_sum(request):
    return render(request, 'elections/polling_units_results_sum.html')