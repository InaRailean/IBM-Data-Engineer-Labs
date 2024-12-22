import pandas as pd
import sqlite3

conn = sqlite3.connect("STAFF.db")

table_name = "Departments"
attribute_list = ["DEPT_ID", "DEP_NAME", "MANAGER_ID", "LOC_ID"]

file_path = "/home/project/Accessing_Databases_Lab/Departments.csv"
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = "replace", index=False) 
print("Table is ready")

# View all the entries
query_statement= f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# View only the department names
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Count the total entries
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()








