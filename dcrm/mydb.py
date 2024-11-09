import mysql.connector

# Establish the connection to MySQL server
dataBase = mysql.connector.connect(
    host='localhost',  # Host where MySQL server is running
    user='root',       # MySQL username
    passwd='your_password'  # MySQL password (change it to your actual password)
)

# Prepare a cursor object using the cursor() method
cursorObject = dataBase.cursor()

# Create a new database
cursorObject.execute("CREATE DATABASE Suveer")  # Replace 'Suveer' with your desired database name

print("Database created successfully!")
