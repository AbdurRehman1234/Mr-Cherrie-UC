'''This code would not be run on geeksforgeeks IDE
because required module
are not installed on IDE. Also this code requires
a remote MySQL databaseconnection with valid
Hostname, Dbusername Password and Dbname'''

# Module For Connecting To MySQL database
import MySQLdb

# Function for connecting to MySQL database
def mysqlconnect():
	#Trying to connect
	try:
		db_connection= MySQLdb.connect("localhost","root","","fareastholdingsb_yahoo")
	# If connection is not successful
	except:
		print("Can't connect to database")
		return 0
	# If Connection Is Successful
	print("Connected")

	# Making Cursor Object For Query Execution
	cursor=db_connection.cursor()

	# Executing Query
	cursor.execute("SELECT 52w FROM yahoo ")
    # WHERE 52w= %(high)s", {'high': '2.600 - 3.200'}

	# Above Query Gives Us The Current Date
	# Fetching Data
	m = cursor.fetchone()

	# Printing Result Of Above
	print(f"{m[1]}")

	# Closing Database Connection
	db_connection.close()

# Function Call For Connecting To Our Database
mysqlconnect()
