from film.models import Film
from django import forms
class filmform(forms.ModelForm):
    class Meta:
        model=Film
        fields='__all__'
