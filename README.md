# Flask Login Website

A simple web application with user authentication using Flask, SQLAlchemy, and Flask-Login.

## Features

- User registration and login
- SQLite database integration
- Blueprints for modular application structure
- Password hashing for secure storage

## Project Structure

login-website/
│
├── venv/ # Virtual environment
│
├── website/ # Main application folder
│ ├── init.py # Application factory
│ ├── config.py # Configuration file
│ ├── models.py # Database models
│ ├── views.py # Main views (routes)
│ ├── auth.py # Authentication views (routes)
│ ├── templates/ # HTML templates
│ └── static/ # Static files (CSS, JS, images)
│
├── main.py # Entry point of the application
├── requirements.txt # Python dependencies
└── README.md # Project documentation