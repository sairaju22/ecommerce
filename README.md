# eCommerce Application by using python flask

An eCommerce web application built using Flask that provides a platform for users to shop online, manage carts, and make secure payments using Razorpay. The platform also includes admin features for managing products, categories, and user orders.

## Features

### User Features:
- **User Registration and Login**: Secure user registration and authentication with OTP verification.
- **Product Browsing**: Users can browse products by category and search for specific items.
- **Cart Management**: Add, update, and remove items from the cart.
- **Order Placement**: Make secure payments via Razorpay and track order history.
- **Contact Form**: Users can reach out with their queries or feedback.

### Admin Features:
- **Admin Registration and Login**: Admin authentication with OTP verification.
- **Product Management**: Add, update, and delete products with images.
- **Order Management**: View and manage user orders.
- **Dashboard**: Admin-specific dashboard for overseeing platform activities.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Database**: MySQL
- **Payment Gateway**: Razorpay
- **Other Libraries**:
  - `mysql.connector` for database connectivity
  - `razorpay` for payment integration
  - Custom OTP generation and email utilities

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sairaju22/ecommerce-app.git
   cd ecommerce-app
2.Install the required Python dependencies:
pip install -r requirements.txt

3.Configure the environment:
Set up a MySQL database and update connection details in the app.py.
Add Razorpay API keys in app.py:
RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'

4.Run the application:

python app.py
Access the app at http://127.0.0.1:5000.

5.Database Schema
Tables:
signup: Stores user information (username, mobile, email, address, password).
adminsignup: Stores admin information (name, mobile, email, password).
additems: Stores product details (item ID, name, description, quantity, category, price).
orders: Stores order details (item ID, name, total price, user, quantity).

Key Routes
Public Routes:
/: Welcome page.
/reg: User registration with OTP verification.
/login: User login.
/logout: User logout.
/homepage: Home page displaying products.
/category/<category>: Filter products by category.
/search: Search for products by name.
/contact: Contact form for user queries.


Cart and Orders:
/addcart/<itemid>/<name>/<category>/<price>/<quantity>: Add items to the cart.
/viewcart: View cart items.
/cartpop/<itemid>: Remove items from the cart.
/orders: View user orders.

Admin Routes:
/adminsignup: Admin registration with OTP verification.
/adminlogin: Admin login.
/adminhome: Admin dashboard.
/additems: Add new products.
/updateproducts/<itemid>: Update product details.
/deleteproducts/<itemid>: Delete products.
/status: View product status.

Payment Integration
Razorpay is integrated for secure payment processing.
Users can make payments, and their orders are recorded upon successful verification.
Future Enhancements
Add user reviews and ratings for products.
Enhance search functionality with fuzzy search.
Implement a RESTful API for mobile app integration.

