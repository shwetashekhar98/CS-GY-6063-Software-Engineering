# CS-GY-6063 Software Engineering

This repository contains the project developed for the **CS-GY-6063 Software Engineering** course. It includes the implementation of software engineering principles, best practices, and a structured approach to building scalable and maintainable applications.

## 📌 Project Overview

This project aims to demonstrate the application of software engineering methodologies, including:
- Software design patterns
- Code modularity and maintainability
- Backend and frontend integration
- Testing and debugging techniques
- Deployment strategies

## 📁 Project Structure

CS-GY-6063-Software-Engineering/ │── cv_resume/ # Main application folder │ ├── templates/ # HTML templates for the frontend │ ├── static/ # Static files like CSS, JavaScript, and images │ ├── app.py # Main application script │ ├── models.py # Database models (if applicable) │ ├── routes.py # Application routes and API endpoints │ ├── requirements.txt # Dependencies and package requirements │ ├── README.md # Project documentation │── tests/ # Unit and integration tests │── docs/ # Documentation files (if any) │── .gitignore # Git ignore file │── setup.py # Setup script for installation (if required)


## 🛠 Installation & Setup

### Prerequisites
Ensure you have the following installed before proceeding:
- Python 3.x
- Pip (Python package manager)
- Virtual environment (`venv`)

### Steps to Run the Project

#### Clone the Repository
```bash
git clone https://github.com/shwetashekhar98/CS-GY-6063-Software-Engineering.git
cd CS-GY-6063-Software-Engineering

### Create a virtual env
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install django

python manage.py runserver



