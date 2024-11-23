# Customer & Product Management Application

A **Python-based desktop application** designed to manage customers and products, featuring integration with **MongoDB** for product data storage and JSON for customer data persistence. It leverages `rich` for a visually appealing console interface.

---

## Technologies Used

<p align="left">
 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="Python" width="40" height="40"/>
  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Rich_%28Python_library%29_logo.svg/2560px-Rich_%28Python_library%29_logo.svg.png" alt="rich" width="40" height="60"/>
  
<img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Mongodb.png" alt="mongoDB" width="60" height="40"/>
</p>

---

## Features

### Customers Module

- **Add new customers**: Create customer profiles with fields like name, age, and unique ID.
- **View all customers**: Display a list of customers from a JSON file.
- **Edit customer profiles**: Update customer details interactively.
- **Delete customers**: Remove unwanted customer profiles.

### Products Module

- **Add new products**: Insert product information into a MongoDB database.
- **View all products**: Retrieve and display a list of products from the database.
- **Edit product information**: Update product details like name, price, or type.
- **Delete products**: Remove products from the database.
- **Search products**: Find specific products by name or filter by type.

### General Features

- **Error handling**: Ensures smooth operation with user-friendly error messages.
- **Rich console UI**: Provides an intuitive interface using the `rich` library.
- **Data persistence**:
  - Customers: Stored in a local JSON file.
  - Products: Managed in a MongoDB collection.

---

## Prerequisites

1. **Python 3.8+**
2. **MongoDB Database** (for products module)
3. **Environment Variables**:
   Create a `.env` file in the root directory with the following:
   ```env
   MONGODB_USERNAME=<your_username>
   MONGODB_PWD=<your_password>
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Installation & Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Set up Environment**:

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure your MongoDB connection in the `.env` file.

3. **Run the Application**:
   ```bash
   python main.py
   ```
