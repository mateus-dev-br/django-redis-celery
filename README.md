# Django Redis Celery Project

This project demonstrates how to configure Django with Redis and Celery for asynchronous email sending.

## Features

- Asynchronous email delivery using Celery
- Integration with Redis as a message broker
- Simple Django web application structure

## Installation

To get started with the project, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/django-redis-celery.git

# Navigate to the project directory
cd django-redis-celery

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

- Python 3.x
- Redis
- Celery

## Usage

To run the application, execute:

```bash
# Start Redis server
redis-server

# Start your Celery worker
celery -A project worker --loglevel=info

# Run the Django development server
python manage.py runserver
```

## Configuration

Make sure to configure your `.env` file with the following variables:

```dotenv
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
DEBUG=True
```
