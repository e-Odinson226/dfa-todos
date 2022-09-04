from django.contrib import admin
from .models import TodoModel


class TodoAmdin(admin.ModelAdmin):
    list_display = ("title", "body")


admin.site.register(TodoModel, TodoAmdin)
