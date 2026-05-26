# Business Requirements Document (BRD)

## 1. Project Summary

**Project name:** Student Task Manager Web App  
**Author:** Горкун Ярослав  
**Document type:** Business Requirements Document

Student Task Manager is a web application for managing educational tasks.  
It helps students organize their practical assignments, documentation tasks and study-related activities.

## 2. Business Goal

The main business goal of the project is to provide a simple and accessible tool for task organization.  
The application allows users to manage their tasks in one place and reduce the risk of forgetting important study activities.

## 3. Problem Statement

Students often have several assignments, reports and practical works at the same time.  
Without a simple task management tool, it becomes harder to track what has already been completed and what still needs attention.

The project solves this problem by providing a minimal task manager with a web interface and API.

## 4. Target Users

The target users are:

- students;
- beginner developers;
- teachers who need a demo CRUD project;
- users who need a simple task tracking tool.

## 5. Business Requirements

### BR-1. Task Visibility

Users must be able to view all created tasks.

### BR-2. Task Creation

Users must be able to create new tasks using a simple form.

### BR-3. Task Completion Tracking

Users must be able to mark tasks as completed or not completed.

### BR-4. Task Removal

Users must be able to delete tasks that are no longer needed.

### BR-5. API Documentation

The project must contain API documentation using Swagger/OpenAPI.

## 6. Stakeholders

| Stakeholder | Interest |
|---|---|
| Student | Complete practical work and demonstrate project documentation |
| Teacher | Review project structure, documentation and API endpoints |
| End user | Manage tasks through a simple interface |

## 7. Business Value

The project provides the following value:

- improves task organization;
- demonstrates web programming skills;
- demonstrates REST API implementation;
- includes technical and business documentation;
- can be expanded into a larger productivity system.

## 8. Success Criteria

The project is successful if:

- the web page opens in a browser;
- tasks can be created;
- tasks can be viewed;
- tasks can be marked as completed;
- tasks can be deleted;
- SSD document is present;
- BRD document is present;
- Swagger/OpenAPI file describes at least two endpoints.

## 9. Assumptions

- The system is used for educational purposes.
- The number of tasks is small.
- Data persistence is not required for the current version.
- The user runs the project locally.

## 10. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| No database storage | Data disappears after server restart | Add database in future version |
| No authentication | Anyone can use local API | Add authentication if deployed |
| Simple UI | Limited functionality | Improve interface later |
| Local-only project | Not accessible publicly | Deploy to hosting if required |

## 11. Conclusion

Student Task Manager satisfies the requirements of the DOCS practical work.  
It contains a working web application, API endpoints, SSD, BRD and Swagger/OpenAPI documentation.
