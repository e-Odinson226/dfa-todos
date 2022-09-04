from rest_framework import serializers

from .models import TodoModel


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = (
            "id",
            "title",
            "body",
        )
