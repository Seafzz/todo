from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.


class TaskModelTest(TestCase):
    def setUp (self):
        self.task = Task.objects.create(title="Test Task", description="This is a test task", completed=False)

    def tesk_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertEqual(self.task.completed)
    
    def test_string_representation(self):
        self.assert_Equal(str(self.task), self.task.title)
        
