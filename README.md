Overview
This is a Django Rest Framework (DRF) based e-commerce API that allows users to browse products, create accounts, add products to the cart, and complete purchases. It provides a structured and scalable backend for an online store.

Features
User Authentication: Register, login, and manage user accounts
Product Management: List, retrieve, create, update, and delete products (Admin only)
Cart System: Add, update, and remove items from the cart
Order Processing: Users can place orders and view their order history
Payment Integration: (Optional) Stripe/PayPal integration for online payments
JWT Authentication: Secure authentication using JSON Web Tokens
Admin Panel: Manage products, orders, and users via Django admin
Technologies Used
Backend: Django, Django Rest Framework (DRF)
Database: SQLite
Version Control: Git & GitHub
Installation & Setup  
1. Clone the repository:  
   `bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
.2 Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
.3 Install dependencies:
pip install -r requirements.txt
.4 Run migrations and start the server:
python manage.py migrate
python manage.py runserver



