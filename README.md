# My-Shop

A fully-featured e-commerce platform built with Django.

## Features

- Product catalog with categories
- Product details with images and features
- Shopping cart functionality
- User authentication and account management
- Order processing and tracking
- Jalali (Persian) date support

## Tech Stack

- Django 5.1.2
- Python 3.x
- SQLite database
- Django Jalali for Persian date support
- Kavenegar integration for SMS notifications

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/My-Shop.git
   cd My-Shop
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   # For Windows
   .venv\Scripts\activate
   # For Linux/Mac
   source .venv/bin/activate
   ```

3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Copy `.env-example` to `.env` and fill in your specific settings.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

- **shop**: Product catalog, categories, and product details
- **cart**: Shopping cart functionality
- **orders**: Order processing and management
- **account**: User authentication and profile management
- **base**: Core project settings and configuration 