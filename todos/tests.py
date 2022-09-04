from urllib import response
from django.test import TestCase
from .models import TodoModel


class TodoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = TodoModel.objects.create(
            title="testing title",
            body="test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body",
        )

    def test_TodoModel_data(self):
        self.assertEqual(self.todo.title, "testing title")
        self.assertEqual(
            self.todo.body,
            "test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body\
            test todo body test todo body test todo body",
        )
        self.assertEqual(str(self.todo), "testing title")
