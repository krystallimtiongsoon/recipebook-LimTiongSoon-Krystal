from django.urls import path
from .views import RecipesListView, RecipeDetailView, RecipeCreateView, ImageCreateView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name="recipes_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_details"),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', ImageCreateView.as_view(), name='image_add'),
]

app_name = 'ledger'
