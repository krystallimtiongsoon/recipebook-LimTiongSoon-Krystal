from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    list_display = ['recipe', 'recipe_image']


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInline, RecipeImageInline]
    search_fields = ('name',)


admin.site.register(Recipe, RecipeAdmin)
