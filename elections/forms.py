from django import forms

class PollingUnitResultsForm(forms.Form):
    polling_unit_uniqueid = forms.IntegerField()


class LgaForm(forms.Form):
    lga_id = forms.IntegerField()