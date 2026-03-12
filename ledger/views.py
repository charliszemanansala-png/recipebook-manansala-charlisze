from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm

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
    return render(request, 'recipe_detail.html', ctx)

@login_required
def add_recipe(request):
    form = RecipeForm()
    if(request.method == "POST"):
        form = RecipeForm(request.POST)
        if form.is_valid():
           r = Recipe()
           r.name = form.cleaned_data.get('name')
           r.author = request.user.profile
           r.save()

           return redirect('ledger:recipe_list')
        
    ctx = {"form": form}
    return render(request, 'add_recipe.html', ctx)

@login_required
def add_image(request, pk):
    form = RecipeImageForm()
    recipe = Recipe.objects.get(pk=pk)

    if(request.method == "POST"):
        form = RecipeImageForm(request.POST, request.FILES)
        
        if form.is_valid():
           i = form.save(commit=False)
           i.recipe = recipe
           i.save()

           return redirect(recipe.get_absolute_url())
        
    ctx = {"form": form, "recipe": recipe}
    return render(request, 'add_image.html', ctx)


           