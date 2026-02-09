from django.urls import path
from .views import recipes_list , recipe_1#, TaskListView

urlpatterns = [
    path('recipes/list', recipes_list,name="recipes_list"),
    path('recipe/1', recipe_1, name="recipe_1"),
    # path('recipe/2', TaskListView.as_view(), name="task_list"),
]

app_name='ledger'