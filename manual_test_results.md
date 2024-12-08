# Manual Test Results

## Test Plan

| Test Case Description                 |   Expected Result                         | Actual Result                          |
| ------------------------------------  |  ---------------------------------------  | ---------------------------------------|
| Verify user can create a task         |  Task is created and visible in task list | Task created successfully              |
| Verify user can edit a task           |  Task details are updated                 | Task edited successfully               |
| Verify user can delete a task         |  Task is removed from the task list       | Task deleted successfully              |
| User can mark a task as completed     |  Task will be marked complete successfully | Task was marked successfully           |
| User signup                           |  User account is created and user is redirected to Tasks | User account was created successfully and redirected to tasks |
| User login                            |  User is logged in and redirected to the homepage | User was logged in and redirected to the homepage |
| Profile update                        |  Profile details are updated              | Profile details were updated successfully |
| Admin dashboard access                |  Admin dashboard is accessible and shows user statistics | Admin dashboard accessed successfully  |
| Role-based access control             |  Normal user will neither have the possibility to see the dashboard icon nor use URL to access admin dashboard | Normal user couldn't see the dashboard icon or use the URL to get access to the dashboard |
| Form validation                       |  Appropriate messages are displayed       | Appropriate messages were displayed, but shown in Swedish during tests |

## Test Evidence

### Task Creation
- ![Task Creation](manual_test_evidence/task_creation.png)

### Task Editing
- ![Task Editing](manual_test_evidence/task_editing.png)

### Task Deletion
- ![Task Deletion](manual_test_evidence/task_deletion.png)

### User Signup
- ![User Signup](manual_test_evidence/user_signup.png)

### User Login
- ![User Login](manual_test_evidence/user_login.png)

### Profile Update
- ![Profile Update](manual_test_evidence/profile_update.png)

### Admin Dashboard Access
- ![Admin Dashboard Access](manual_test_evidence/admin_dashboard_access.png)

### Role-Based Access Control
- ![Role-Based Access Control](manual_test_evidence/role_based_access_control.png)

### Form Validation
- ![Form Validation](manual_test_evidence/form_validation.png)
