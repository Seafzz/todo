from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.


class TaskModelTest(TestCase):
    def setUp(self):
        #create user
        self.user = User.objects.create_user(username='testuser', password='testproject4')
        
        self.task = Task.objects.create( 
            title="Test Task", description="This is a test task", completed=False, user=self.user)

        #login user
        self.client.login(username='testuser', password='testproject4')

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user, self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.task), self.task.title)


class TaskViewTests(TestCase):
    def setUp(self):
        # Create user 
        self.user = User.objects.create_user(username='testuser', password='testproject4')

        self.task = Task.objects.create( title="Test Task", description="This is a test task", completed=False, user=self.user)

        # Login user 
        self.client.login(username='testuser', password='testproject4')

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'tasks/task_detail.html')