from django import forms
from .models import Masjid


class MasjidCreateForm(forms.ModelForm):

    your_contact = forms.CharField(widget=forms.TextInput(
        attrs={"minlength": 10, "maxlength": 10, "pattern": "\d", "placeholder": "9876543210"}))

    fajar = forms.TimeField(input_formats=["%I:%M %p"])
    zuhar = forms.TimeField(input_formats=["%I:%M %p"])
    asar = forms.TimeField(input_formats=["%I:%M %p"])
    maghrib = forms.TimeField(input_formats=["%I:%M %p"])
    isha = forms.TimeField(input_formats=["%I:%M %p"])
    juma = forms.TimeField(input_formats=["%I:%M %p"])

    class Meta:
        model = Masjid
        fields = ("name", "area", "address", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")


class MasjidUpdateForm(forms.ModelForm):

    fajar = forms.TimeField(input_formats=["%I:%M %p"])
    zuhar = forms.TimeField(input_formats=["%I:%M %p"])
    asar = forms.TimeField(input_formats=["%I:%M %p"])
    maghrib = forms.TimeField(input_formats=["%I:%M %p"])
    isha = forms.TimeField(input_formats=["%I:%M %p"])
    juma = forms.TimeField(input_formats=["%I:%M %p"])

    class Meta:
        model = Masjid
        fields = ("name", "area", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
        non_editable_fields = ("name", "area")

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['area'].disabled = True
