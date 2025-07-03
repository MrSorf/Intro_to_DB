import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user & password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # ← Replace this with your real MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # Close connection if it was opened
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed")  # Optional: remove comment to print

# Run the function
create_database()
