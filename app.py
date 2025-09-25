from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'b9f3a6c0e91f4d1ba9189c4ea7f0d9af'

@app.context_processor
def inject_date():
    """Injects the current date and time into all templates."""
    return dict(now=datetime.utcnow())

# Database connection
def get_db_connection():
    """Establishes a connection to the database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kumbh"
    )

@app.route('/')
def index():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/book_ticket', methods=['GET', 'POST'])
def book_ticket():
    """Handles ticket booking form submission and renders the booking page."""
    if request.method == 'POST':
        name = request.form['name']
        id_proof = request.form['id_proof']
        ticket_type = request.form['ticket_type']

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO tickets (name, id_proof, ticket_type, booking_time)
                VALUES (%s, %s, %s, %s)
            """, (name, id_proof, ticket_type, datetime.now()))

            connection.commit()
            ticket_id = cursor.lastrowid
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", "danger")
            return redirect(url_for('book_ticket'))
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
        
        flash(f"Ticket Booked Successfully! Your Ticket ID is: {ticket_id}", "success")
        return redirect(url_for('ticket_details', ticket_id=ticket_id))

    ticket_types = ['General', 'VIP', 'Seva Darshan']
    return render_template('book_ticket.html', ticket_types=ticket_types)

@app.route('/ticket/<int:ticket_id>')
def ticket_details(ticket_id):
    """Displays the details for a specific ticket."""
    ticket = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,))
        ticket = cursor.fetchone()
    except mysql.connector.Error as err:
        flash(f"Database error: {err}", "danger")
        return redirect(url_for('index'))
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    if not ticket:
        flash("Ticket not found!", "danger")
        return redirect(url_for('index'))

    return render_template('ticket_details.html', ticket=ticket)

@app.route('/view_ticket', methods=['GET', 'POST'])
def view_ticket():
    """Handles the form to look up a ticket by its ID."""
    if request.method == 'POST':
        ticket_id = request.form.get('ticket_id')
        if ticket_id:
            return redirect(url_for('ticket_details', ticket_id=ticket_id))
        else:
            flash("Please enter a Ticket ID.", "warning")
    return render_template('view_ticket.html')

if __name__ == '__main__':
    app.run(debug=True)