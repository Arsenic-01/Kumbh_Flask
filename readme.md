# Kumbh Mela Ticket Management System

A simple, clean, and professional web application built with **Flask** and **MySQL** for booking and managing tickets for the Kumbh Mela event. This project serves as a straightforward example of a full-stack Python web application.

---

## ✨ Features

* **User-Friendly Interface**: A modern and responsive design that works on all devices.
* **Ticket Booking**: A simple form to book new tickets with essential details like name, ID proof, and ticket type.
* **Ticket Viewing**: Easily retrieve and view the details of any booked ticket using its unique ID.
* **Real-time Feedback**: Dynamic flash messages to inform users of successful bookings or errors.
* **Direct Database Integration**: Connects to a MySQL database to persist all booking information.

---

## 🛠️ Tech Stack

* **Backend**: Python with the Flask framework
* **Database**: MySQL (connected via `mysql-connector-python`)
* **Frontend**: HTML5, CSS3, and the Jinja2 templating engine

---

## 🚀 Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

* Python 3.x installed on your system
* MySQL Server installed and running

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd Kumbh_Flask
```

### 3. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies

Create a file named `requirements.txt` in your project root with the following content:

```txt
Flask
mysql-connector-python
```

Now, install the packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Database Setup

Log in to your MySQL server and create a new database:

```sql
CREATE DATABASE kumbh;
```

Use the new database and create the `tickets` table:

```sql
USE kumbh;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    id_proof VARCHAR(255) NOT NULL,
    ticket_type VARCHAR(50) NOT NULL,
    booking_time DATETIME NOT NULL
);
```

### 6. Configure the Application

Open `app.py` and ensure the database connection details in the `get_db_connection` function match your local MySQL setup.

```python
# app.py

def get_db_connection():
    """Establishes a connection to the database."""
    return mysql.connector.connect(
        host="localhost",      # Your MySQL host
        user="root",           # Your MySQL username
        password="",           # Your MySQL password
        database="kumbh"       # The database you created
    )
```

### 7. Run the Application

Start the Flask development server:

```bash
flask --app app run
```

The application will be running at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 Usage

1. Navigate to the home page (`/`) to see the main menu.
2. Click on **"Book a Ticket"** to go to the booking form (`/book_ticket`).
3. Fill in your details and submit the form. You'll receive a success message with your new Ticket ID.
4. Navigate to **"View Your Ticket"** (`/view_ticket`) and enter your Ticket ID to see your booking details.
