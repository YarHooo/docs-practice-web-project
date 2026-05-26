# System Specification Document (SSD)

## 1. Project Overview

**Project name:** Student Task Manager Web App  
**Project type:** Web application with REST API  
**Author:** Горкун Ярослав  
**Technology stack:** Python, Flask, HTML, CSS, JavaScript

Student Task Manager is a simple web application that allows users to manage student tasks.  
The application provides a browser interface and REST API endpoints for creating, viewing, updating and deleting tasks.

## 2. System Purpose

The purpose of the system is to provide a simple tool for organizing educational tasks.  
The project demonstrates the implementation of a web application with frontend, backend, REST API and API documentation.

## 3. System Scope

The system includes:

- frontend web interface;
- backend Flask server;
- REST API for task management;
- in-memory task storage;
- OpenAPI/Swagger endpoint documentation;
- project documentation.

The system does not include:

- user authentication;
- permanent database storage;
- role-based permissions;
- cloud deployment.

## 4. Functional Requirements

### FR-1. View Tasks

The system shall allow users to view all available tasks.

**Endpoint:** `GET /api/tasks`

### FR-2. Create Task

The system shall allow users to create a new task by entering its title.

**Endpoint:** `POST /api/tasks`

### FR-3. Update Task Status

The system shall allow users to update the completion status of a task.

**Endpoint:** `PATCH /api/tasks/{id}`

### FR-4. Delete Task

The system shall allow users to delete a task by its identifier.

**Endpoint:** `DELETE /api/tasks/{id}`

## 5. Non-Functional Requirements

### 5.1 Performance

The system should respond quickly to user actions and API requests for a small amount of task data.

### 5.2 Usability

The interface should be simple, clear and easy to use.

### 5.3 Compatibility

The web interface should work in modern browsers such as Google Chrome, Mozilla Firefox, Microsoft Edge and Safari.

### 5.4 Maintainability

The code should be separated into backend logic, frontend markup, styles and scripts.

## 6. System Architecture

The application uses a client-server architecture.

- The frontend is built with HTML, CSS and JavaScript.
- The backend is built with Flask.
- JavaScript sends HTTP requests to Flask API endpoints.
- The backend returns JSON responses.
- Data is stored in memory during application runtime.

## 7. Data Model

### Task

| Field | Type | Description |
|---|---|---|
| id | integer | Unique task identifier |
| title | string | Task title |
| completed | boolean | Task completion status |

Example:

```json
{
  "id": 1,
  "title": "Prepare SSD document",
  "completed": false
}
```

## 8. API Specification Summary

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks` | Get all tasks |
| POST | `/api/tasks` | Create new task |
| PATCH | `/api/tasks/{id}` | Update task |
| DELETE | `/api/tasks/{id}` | Delete task |

## 9. Error Handling

The system returns JSON error messages for invalid requests.

Examples:

- `400 Bad Request` — task title is missing;
- `404 Not Found` — task with requested ID does not exist.

## 10. Security Considerations

The project is educational and does not include authorization.  
Basic security considerations include:

- validation of required request fields;
- separation of frontend and backend logic;
- controlled API routes.

## 11. Future Improvements

Possible future improvements:

- add database storage;
- add user authentication;
- add deadline field for tasks;
- add task categories;
- deploy project to a public server;
- add full Swagger UI page.
