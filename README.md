# Task Manager

Task Manager is a web application designed to help users manage their tasks efficiently. It allows users to create, view, update, and delete tasks, as well as mark tasks as completed.

## Features

- User authentication: Users can sign up, log in, and log out securely.
- Task management: Users can create new tasks, view their existing tasks, update task details, mark tasks as completed, and delete tasks.
- Pagination: Tasks are paginated to improve performance and user experience.
- Responsive design: The application is designed to work seamlessly across devices of all sizes, including desktops, tablets, and smartphones.
- Customizable templates: The application uses Django templates with Tailwind CSS, allowing for easy customization of the user interface.

## Tech Stack

- **Django**: The web application framework used for building the backend.
- **Django Allauth**: Provides user authentication functionality, including signup, login, and logout.
- **HTML/CSS/JavaScript**: Frontend technologies used for designing and implementing the user interface.
- **Tailwind CSS**: A utility-first CSS framework for rapidly building custom designs.
- **PostgreSQL**: A powerful open-source relational database used for storing user data and task information.
- **Python 3.x**: The programming language used for backend development.

## Getting Started

To run the Task Manager locally on your machine, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd task-manager`
3. Install the dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Create a superuser (admin): `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Access the application in your web browser: `http://localhost:8000`
