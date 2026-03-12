from django.urls import path
from .views import recipe_list, recipe_detail, add_recipe, add_image

app_name = "ledger"

urlpatterns = [
    path('recipes/list/', recipe_list, name ='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe-detail'),
    path('recipe/<int:pk>/add_image', add_image, name="add_image"),
    path('recipe/add/', add_recipe, name='add_recipe'),

]