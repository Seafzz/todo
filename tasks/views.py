from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib import messages
from .forms import ProfileForm
from .forms import TaskForm
from .models import Profile
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def toggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'tasks/update_profile.html', {'form': form})


@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'tasks/view_profile.html', {'profile': profile})


def home(request):
    return render(request, 'tasks/home.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='admin').exists()

@user_passes_test(is_admin)
def admin_dashboard_view(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    return render(request, 'admin/dashboard.html', {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    })
