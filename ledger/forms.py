from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class eta:
        model = Recipe
        fields = '__all__'