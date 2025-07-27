# Sweet Shop Management – Frontend
(React Application)

# Project Overview:
The frontend of the Sweet Shop Management System has been developed using React.js. It serves as the user interface through which both customers and administrative users interact with the backend API services. The system provides secure, role-based access and a clean, responsive interface for sweet catalog management and purchase operations.

The application supports authentication via JWT, and its structure allows conditional rendering of features based on the user's role (customer or admin). Customers are able to view and purchase sweets, while administrators have privileges to manage the inventory.

# Core Functionalities:

## User Authentication:

   * Registration form accepting first name, last name, username, email, password, and user role (admin or customer).
   * Login form with JWT-based authentication.
   * User-specific feedback for successful or invalid login and registration attempts.

## Customer Capabilities:

   * View all available sweets with details such as name, price, category, and quantity in stock.
   * Search sweets by unique ID.
   * Purchase sweets by entering desired quantity.
   * Display of feedback messages when attempting to purchase unavailable or out-of-stock items.
   * Purchase functionality is only available to logged-in users.

## Admin Functionalities:

   * Add new sweets by specifying name, category, price, and quantity.
   * Update existing sweet details partially or completely.
   * Delete sweets from the catalog.
   * Restock items by increasing their available quantity.
   * Admin panel access is strictly restricted to authenticated admin users.

## User Interface and Experience:

   * Clean and bright design for intuitive navigation.
   * Responsive layout that adapts to different screen sizes (desktop, tablet, mobile).
   * Real-time alerts and feedback messages upon successful or failed operations.
   * Role-based rendering of components and features.

## Execution and Setup:
The frontend application is developed using React and can be run locally using Node.js. After installing project dependencies using npm, the development server can be launched, allowing access to the application through the browser. The frontend is designed to interact with the backend via RESTful APIs. API endpoints are integrated using Axios, and any required changes to backend URLs can be adjusted within the frontend service configuration files.

## AI Usage Disclosure:
To support the frontend development process, AI tools such as ChatGPT and GitHub Copilot were utilized. These tools assisted in generating form validation logic, component structures, and layout ideas. However, all business logic, API integrations, and user interface decisions were implemented and reviewed manually by the developer.

# ScreenShots pdf:[Sweets_shop.pdf](https://github.com/user-attachments/files/21455888/Sweets_shop.pdf)

