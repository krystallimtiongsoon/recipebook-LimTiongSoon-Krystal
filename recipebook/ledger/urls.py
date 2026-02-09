from django.urls import path
from .views import recipes_list #, task_list, TaskListView

urlpatterns = [
    path('recipes/list', recipes_list,name="recipes_list"),
    # path('recipe/1', TaskListView.as_view(), name="task_list"),
    # path('recipe/2', TaskListView.as_view(), name="task_list"),
]

app_name='ledger'