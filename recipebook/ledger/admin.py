from django.contrib import admin
from .models import Recipe, RecipeIngredient


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInline,]
    search_fields = ('name',)


admin.site.register(Recipe, RecipeAdmin)
