from django.urls import path
from .views import ListTodoView, DetailTodoView

urlpatterns = [
    path("", ListTodoView.as_view(), "todo-list-api"),
    path("<int:pk>/", DetailTodoView.as_view(), "todo-detail-api"),
]
