import mysql.connector

# Establish the connection to MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='your-password'  # Use your actual password
)

# Create a cursor object using the connection
cursorObject = dataBase.cursor()

# Create a new database called 'Suveer'
cursorObject.execute("CREATE DATABASE Suveer")

# Print success message
print("All Done!")

