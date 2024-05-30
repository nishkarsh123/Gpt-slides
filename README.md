# Django Project Setup Guide

This comprehensive guide assists developers in setting up and running a Django-based application leveraging Redis for task management and Open Ai for editing PPT slides.

## Prerequisites

Before proceeding with the setup, ensure the following components are installed and configured on your system:

### Redis

- **Option 1: Install Redis natively**
  - Follow the detailed installation instructions for Redis available at [Redis Official Documentation](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/).

- **Option 2: Run Redis via Docker**
  - If Docker is installed on your system, you can start a Redis container with the following command:

    ```bash
    docker run -d --name redis -p 6379:6379 redis:7.2-alpine
    ```

### Open AI Account

- **Create an Account**:
  - Register at Open AI's website to obtain an API key necessary for Custom Agent. New accounts typically receive initial credits for free usage.
  - Visit the website and follow the sign-up process.

### Python

- Ensure Python 3.8 or higher is installed on your system. You can verify this by running:

  ```bash
  python --version
  ```

## Installation Steps

Follow these steps to configure your development environment and launch the application.

### 1. Set up the Python Virtual Environment

- **Creation**:

  ```bash
  python -m venv env
  ```

- **Activation**:

  ```bash
  source env/bin/activate  # On Unix/macOS
  env\Scripts\activate  # On Windows
  ```

### 2. Install Required Python Packages

- Install all dependencies listed in the `requirements.txt` to ensure all required libraries are available.

  ```bash
  pip install -r requirements.txt
  ```

### 3. Configure Environment Variables

- Create a `.env` file in the root of your project directory and populate it with necessary configuration:

  ```plaintext
  OPENAI_API_KEY=<Your Stability API Key>
  CELERY_BROKER=redis://localhost:6379/0
  ```

### 4. Initialize the Database

- Apply migrations to set up your database schema:

  ```bash
  python manage.py migrate
  ```

### 5. Create an Administrative User

- Start the interactive prompt to create a superuser account:

  ```bash
  python manage.py createsuperuser
  ```

### 6. Launch the Development Server

- Start the Django development server:

  ```bash
  python manage.py runserver
  ```

### 7. Start Celery Worker

- In a new terminal session, initiate a Celery worker to handle background tasks:

  ```bash
  celery --app=gpt_slides worker --loglevel=info
  ```

### 8. Start Celery Flower (Optional)

- To monitor and manage Celery tasks via a web interface, run Celery Flower:

  ```bash
  FLOWER_UNAUTHENTICATED_API=True celery -A core --broker=redis://localhost:6379/0 flower --port=5555
  ```