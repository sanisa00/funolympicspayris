# FunOlympic Games Online Registration System

## Introduction
[Product Development Scenario]The City of Payris is proud to host the upcoming FunOlympic Games in 2024. As part of the commitment to delivering a seamless and inclusive experience, I have developed an online registration system. This platform enables global audiences to register, login, and select broadcasts they wish to watch, ensuring the games are accessible to everyone, anywhere.

## Features

### Public User Features
- **User Registration**: Sign up with personal details including name, country, email address, contact number, and preferred sports.
- **Login/Logout Functionality**: Secure access to user accounts.
- **Broadcast Selection**: Personalize your viewing experience by selecting the sports broadcasts you're interested in.

### Admin Features
- **User Management**: View and manage user registrations.
- **Interaction Overview**: Monitor user interactions and preferences.
- **Event Management**: Manage events.

## Getting Started

### Prerequisites
- Python 3.10+
- Django 5.0.1+
- 

### Installation
1. Clone the project repository:
git clone https://github.com/sanisa00/funolympicspayris.git

2. Navigate to the project directory:
cd funcolympicspayris

3. Install required dependencies:
pip install -r requirements.txt


### Setting Up the Environment
1. Set up the Django secret key in your environment variables.
2. Configure your database in `settings.py`.
3. Apply migrations to set up the database schema:
python manage.py migrate
4. Create an admin user for the admin dashboard:
python manage.py createsuperuser


### Running the Application
- Start the development server:
python manage.py runserver

- Access the application at `http://127.0.0.1:8000` and the admin panel at `http://127.0.0.1:8000/admin`.

## Usage Guide
For detailed instructions on how to use the system, mail the creator of this project.
