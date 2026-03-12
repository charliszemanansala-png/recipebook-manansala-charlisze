from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage
class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display =('id', 'name')
    search_fields = ("name", )
    inlines = [RecipeIngredientInLine, RecipeImageInLine]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe__name', 'ingredient__name' )
    list_display = ('recipe', 'ingredient', 'quantity' )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeImage)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
