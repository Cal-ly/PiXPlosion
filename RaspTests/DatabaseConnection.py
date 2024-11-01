import pyodbc

# Define the connection string parameters
server = 'mssql8.unoeuro.com'  # e.g., 'localhost' or 'SERVERNAME'
database = 'nkof_dk_db_flexible'  # The name of your database
username = 'nkof_dk'  # Your SQL Server username (if needed)
password = 'w9cpe6AaR4yHBxbdDr3g'  # Your SQL Server password (if needed)

# Create a connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Create a cursor object to execute queries
    cursor = conn.cursor()

    # Example: Execute a sample query
    cursor.execute("SELECT * FROM dbo.RaspberryPi")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error connecting to SQL Server:", e)

finally:
    # Close the connection
    if 'conn' in locals():
        conn.close()