Sweet Shop Management – Backend
Project Overview
This backend application serves as the core API service for the Sweet Shop Management System. Built using Django and Django REST Framework, it is responsible for managing user authentication, sweet inventory operations, and purchase transactions. The system supports two roles: admin and customer. Admin users have elevated privileges to manage the sweet catalog, while customers are allowed to browse and purchase available items.
All endpoints are protected using JWT-based authentication, and access is controlled based on user roles. The project was developed following a test-driven development (TDD) approach using Django’s built-in testing framework.

Features
Secure user registration and login
Role-based access control (admin vs customer)
Create, update, delete, and restock sweets (admin only)
Search and retrieve sweet details by ID
Purchase sweets with quantity validation
RESTful API architecture with clean, modular code

Setup & Execution
To run the backend locally:

Clone the repository and navigate to the backend directory.

Create a Python virtual environment and activate it.

Install the project dependencies using pip.

Configure your MySQL database in settings.py.

Apply migrations and create a superuser.

Start the development server using Django’s runserver command.

The server will be accessible at http://localhost:8000.

Testing
All backend functionalities are validated through automated tests written using Django’s APITestCase module. These tests cover authentication, CRUD operations, purchase logic, and helper methods.

To run the tests

python manage.py test

This will execute the full suite and display a summary of passed and failed tests in the terminal.

Test Report:
[Test_report.md](https://github.com/user-attachments/files/21455499/Test_report.md)

AI Usage Disclosure:
The backend project was supported by AI tools to enhance development efficiency. ChatGPT was used to assist with test scaffolding and commit documentation. GitHub Copilot provided code suggestions for repetitive patterns. All business logic, validations, and design decisions were implemented manually and thoroughly reviewed by the developer.
