from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                }
            ),
        }
