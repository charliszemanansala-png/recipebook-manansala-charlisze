from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe_Ingredient, Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes': recipes }
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe_Ingredient.objects.all(pk=pk)
    ingredient = recipe.ingredients.all()
    ctx = {'recipes': recipe}
    ctz = {'ingredients': ingredient}
    return render(request, 'recipe_detail.html', ctx, ctz)

recipes = [
        {
            "name": "   Recipe 1",
            "ingredients": [
               {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                   "name": "onion",
                   "quantity": "1pc"
               },   
               {
                    "name": "pork",
                   "quantity": "1kg"
                },      
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {   
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "   Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                }, 
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]     

def recipe_list(request):
    return render(request, 'recipe_list.html', {'recipes' : recipes } )

def recipe_1(request):
    return render(request, 'recipe_detail.html', {'recipe': recipes[0]})

def recipe_2(request):
    return render(request, 'recipe_detail.html', {'recipe': recipes[1]})

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

