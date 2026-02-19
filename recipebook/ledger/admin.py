from django.contrib import admin

from .models import Recipe, Recipe_Ingredient

class Recipe_IngredientInLine(admin.TabularInline):
    model = Recipe_Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display =('id', 'name')
    search_fields = ("name", )
    inlines = [Recipe_IngredientInLine,]

class Recipe_IngredientAdmin(admin.ModelAdmin):
    model = Recipe_Ingredient
    search_fields = ('recipe__name', 'ingredient__name' )
    list_display = ('recipe', 'ingredient', 'quantity' )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Recipe_Ingredient, Recipe_IngredientAdmin)

# Register your models here.
