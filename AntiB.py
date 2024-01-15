# Import the mysql.connector module for MySQL database connectivity
import mysql.connector
# Import the dbconfig module (presumably containing configuration details)
import dbconfig as cfg

# Define a class named AntiB for handling MySQL database operations
class AntiB:
    # Class variables to store database connection details and cursor
    connection = ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""

    # Constructor (__init__) method initializes the connection details from the configuration
    def __init__(self):
        # Retrieve database connection details from the cfg module
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    # Method to get a database cursor for executing queries
    def getcursor(self):
        # Establish a connection to the MySQL database using stored connection details
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        # Create and return a cursor for executing queries
        self.cursor = self.connection.cursor()
        return self.cursor

    # Method to close both the database connection and cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Method to insert a new record into the 'wait_list' table
    def create(self, values):
        # Get a cursor for executing queries
        cursor = self.getcursor()
        # SQL query to insert data into the 'wait_list' table
        sql = "insert into wait_list (Archivedate, Adult_Child, HospitalName, 0-6 Months, 6-12 Months, 12-18 Months, 18 Months+, Total) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        # Execute the query with the provided values
        cursor.execute(sql, values)
        # Commit the changes to the database
        self.connection.commit()
        # Retrieve the last inserted row's ID
        newid = cursor.lastrowid
        # Close the database connection and cursor
        self.closeAll()
        # Return the new row's ID
        return newid

    # Method to retrieve all data from the 'wait_list' table
    def get_all_data(self):
        # Get a cursor for executing queries
        cursor = self.getcursor()
        # SQL query to select all data from the 'wait_list' table
        sql = "SELECT * FROM wait_list"
        # Execute the query
        cursor.execute(sql)
        # Fetch all the data from the query result
        data = cursor.fetchall()
        # Close the database connection and cursor
        self.closeAll()
        # Return the fetched data
        return data

# Create an instance of the AntiB class
antiB_instance = AntiB()
