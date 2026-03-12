from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInline,]
    search_fields = ('name',)


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage


admin.site.register(Recipe, RecipeAdmin)
