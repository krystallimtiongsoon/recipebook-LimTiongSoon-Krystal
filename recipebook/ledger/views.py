from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_details.html"

class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"