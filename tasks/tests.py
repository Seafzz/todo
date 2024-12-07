from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.


class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task", description="This is a test task", completed=False)

    def tesk_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertFalse(self.task.completed)

    def test_string_representation(self):
        self.assert_Equal(str(self.task), self.task.title)


class TaskViewTests(TestCase):
    def setup(self):
        self.task = Task.objects.create(
            title="Test Task", description="This is a test task", completed=False)

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assert_Contains(response, "Test Task")
        self.assertTemplateUsed(respone, 'task/task_list.html')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.asserContains(response, 'Test Task')
        self.assertTemplateUsed(respone, 'tasks/task_list.html')
