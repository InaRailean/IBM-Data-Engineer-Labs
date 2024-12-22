import pandas as pd 
import sqlite3

conn = sqlite3.connect("STAFF.db")

table_name = "INSTRUCTOR"
attribute_list= ["ID", "FNAME", "LNAME", "CITY", "CCODE"]

# Read the csv file
file_path = "/home/project/Accessing_Databases_Lab/INSTRUCTOR.csv"
df = pd.read_csv(file_path, names = attribute_list)

# Loading the data to the table
df.to_sql(table_name, conn, if_exists= "replace", index = False)
print("Table is ready")

# Print the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Print only FNAME column
query_statement = f"SELECT FNAME FROM {table_name}"
query_output= pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Print total number of entries
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output =pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Append data to the table
data_dict = {"ID": [100],
            "FNAME": ["John"],
            "LNAME": ["Doe"],
            "CITY": ["Paris"],
            "CCODE": ["FR"]}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = "append", index= False)
print("Data appended successfully")

# Check the total number of entries after append
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output =pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Close the connection
conn.close()