from django import forms
from .models import Masjid


class MasjidCreateForm(forms.ModelForm):

    your_contact = forms.CharField(widget=forms.TextInput(attrs={"minlength": 10, "maxlength": 10, "pattern": "[6-9]{1}[0-9]{9}", "placeholder": "9876543210"}))

    fajar = forms.TimeField(input_formats=["%I:%M %p"])
    zuhar = forms.TimeField(input_formats=["%I:%M %p"])
    asar = forms.TimeField(input_formats=["%I:%M %p"])
    maghrib = forms.TimeField(input_formats=["%I:%M %p"])
    isha = forms.TimeField(input_formats=["%I:%M %p"])
    juma = forms.TimeField(input_formats=["%I:%M %p"])

    class Meta:
        model = Masjid
        fields = ("name", "area", "address", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")

    def clean(self):
        your_contact = str(self.cleaned_data['your_contact'])
        if len(your_contact) != 10 or not your_contact.isdigit():
            return forms.ValidationError("Phone number is not valid.")
        self.cleaned_data['your_contact'] = "+91" + your_contact
        return super().clean()


class MasjidUpdateForm(forms.ModelForm):

    your_contact = forms.CharField(widget=forms.TextInput(attrs={"minlength": 10, "maxlength": 10, "pattern": "[6-9]{1}[0-9]{9}", "placeholder": "9876543210"}))

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

    def clean(self):
        your_contact = str(self.cleaned_data['your_contact'])
        if len(your_contact) != 10 or not your_contact.isdigit():
            return forms.ValidationError("Phone number is not valid.")
        self.cleaned_data['your_contact'] = "+91" + your_contact
        return super().clean()

