from django.urls import path
from .views import TodoListViewAPI, TodoDetailViewAPI

urlpatterns = [
    path("", TodoListViewAPI.as_view(), name="todo-list-api"),
    path("<int:pk>/", TodoDetailViewAPI.as_view(), name="todo-detail-api"),
]
