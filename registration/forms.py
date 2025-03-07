from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["name", "year", "department", "college", "phone", "email"]  # Exclude player_number
