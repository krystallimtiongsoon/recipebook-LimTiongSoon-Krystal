from django.urls import path
from .views import RecipesListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipesListView,name="recipes_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_detail"),
]

app_name='ledger'