from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes }
    return render(request, 'recipe_list.html', ctx)

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredient = recipe.ingredients.all()
    ctx = {
        'recipe': recipe,
        'ingredients': ingredient,
        }
    return render(request, 'profile_detail.html', {'user': request.user})
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name ='recipe_detail.html'
    context_object_name = 'recipe'