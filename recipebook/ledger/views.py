from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

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

def recipe_1(request):
    return render(request, 'recipe_detail.html', {'recipe': recipes[0]})

def recipe_2(request):
    return render(request, 'recipe_detail.html', {'recipe': recipes[1]})

class RecipeListView(TemplateView):
    template_name = 'recipe_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['recipes'] = recipes
        return context
