from rest_framework import generics

from .models import TodoModel
from .serializers import TodoSerializers


class TodoListViewAPI(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class TodoDetailViewAPI(generics.RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers
