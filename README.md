# Todo List Application

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Agile Methodology](#agile-methodology)
7. [Data Models](#data-models)
8. [Authentication and Authorization](#authentication-and-authorization)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Contributing](#contributing)
12. [Acknowledgements](#acknowledgements)


## Project Overview
The Todo List Application is a full-stack web application built using Django MVC framework. It allows users to manage their tasks efficiently by creating, editing, and deleting tasks.
The app includes user authentication, role-based access control and responsive design to ensure a seamless experience across devices.

## Features
- User authentication (signup, login, logout)
- Role-based access control (admin dashboard)
- Task management (CRUD) (Create, read, update, delete tasks)
- Profile management
- Responsive design
- Notifications for task updates

## Technologies Used
- **Programing Languages**: Python
- **Framework**: Django
- **Frontend**: Bootstrap, HTML, CSS, JavaScript
- **Database**: SQlite (development), PostgresSQL (production)
- **Deployment**: Heroku
- **Version Control**: Git, Github
- **IDE**: Visual Studio Code, GitHub
- **AI Assistance**: Co-Pilot

## Setup and Installation
1. **Clone the repository from Github**: 
git clone https://github.com/Seafzz/todo
2. Install the required packages
pip install -r requirements.txt
3. create a .env file in the project directory and add your configurations
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
DEBUG=False
4. Run the migrations to set up your database:
python manage.py migrate
5. Create a superuser for admin access (Optional, but recommended)
python manage.py createsuperuser
6. start the development server:
python manage.py runserver
7. Your todo list should now run locally! Navigate to http://localhost:8000

## Usage
1. Navigate to http://Localhost:8000 in your webbrowser
2. Sign up for a new account or log in with your credentials.
3. Use the navigation bar to acces the task list, create new tasks and manage your profile
4. Admin users can access the admin dashboard for additional functionalities. 



## Agile Methodology
The project was planned and implemented using Agile methodology.
User stories were documented and managed using Github Project board.

 #### Project Board
  - The project board was divided into columns such as "To Do", "In Progress", and "Done" to visually track the progress of tasks. - **Example Columns**: 
  - To Do 
  - In Progress 
  - Done

The project was planned and implemented using Agile methodology. To provide a comprehensive overview, some of the issues and tasks have been documented retrospectively to reflect the actual development process.


## Data Models

### User
- **Fields**:
- **username**: The unique username for the user.  
- **password**: The user's hashed password. 
- **profile**: One-to-one relationship with the Profile model.

### Profile

Stores additional information about the

- **Fields**: 
- **user**: The related user. 
- **bio**: A short biography of the user. 
- **location**: The user's location. 
- **birth_date**: The user's birth date.

### Task

Represents a task that a user can create, edit, and manage.

- **Fields**: 
- **user**: The user who owns the task. 
- **title**: The title of the task. 
- **description**: A detailed description of the task. 
- **completed**: A boolean indicating if the task is completed. 
- **due_date**: The due date for the task. 
- **created_at**: The timestamp when the task was created. 
- **priority**: The priority of the task (Low, Urgent, Asap). 
- **category**: The category of the task (Work, Personal, Others).

## Authentication and Authorization

### Authentication

User authentication ensures that only registered users can log in and access their account securely.

- **User Signup**: Users can create a new account by providing a username and password.
- **User Login**: Users can log in using their credentials to access their tasks and profile.
- **User Logout**: Users can log out to securely end their session.

### Authorization

Authorization controls what authenticated users are allowed to do within the application. Role-based acces control (RBAC)
-**Standard Users**: Can create, edit and delete their own update their profile; and view their task list.
-**Admins**: Have additional permissions, view task statistics, and access the admin dashboard.


### Security Measures
- **Password Hasing**: User password are hashed before being stored in the database


The application uses decorators such as `@login_required` and `@user_passes_test` to enforce authentication and authorization at the view level.

#### Example Code Snippets

- **Login Required Decorator**: 
```python 
@login_required def task_list(request): 
tasks = Task.objects.filter(user=request.user).order_by('due_date')
 return render(request, 'tasks/task_list.html', {'tasks': tasks}) 
 ```
- **User Passes Test Decorator for Admin Access**:
    ```python
    def is_admin(user):
        return user.is_authenticated and user.groups.filter(name='admin').exists()

    @user_passes_test(is_admin) 
    def admin_dashboard_view(request)
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    return render(request, 'admin/dashboard.html')
    ```
