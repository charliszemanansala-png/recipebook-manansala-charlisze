from django.urls import path
from .views import RecipeListView, recipe_1, recipe_2

app_name = "ledger"

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe-list'),
    path('1/', recipe_1, name='recipe1'),
    path('2/', recipe_2, name='recipe2'),
]