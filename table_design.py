# To Do
# Make sure table name is in database

import pyodbc
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Prompt user for output file
file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=(("txt", "*.txt"), ("all files", "*.*")))

txt_export = open(file_path, 'w')  #

server = 'planet15.database.windows.net'
database = 'ugridd'
username = 'test'
password = input("Enter server password: ")
driver = '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD=' +
                      password)
cursor = cnxn.cursor()
table_name = ''  # Define variable for table name to be used
table_list = []  # Empty list for tables in uGRIDD DB
col_list = []  # Create empty column list
typelist = []  # Create empty type list

cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
tables = cursor.fetchall()  # Create list of tables in uGRIDD Database

for table in tables:
    table_list.append((table[0]).lower())


while True:
    table_name = input('Type table name: ').lower()  # Ask user for table name
    if table_name in table_list:
        break
    print("Table not in database.")

print('')  # Print blank line

# Query to return all column names
cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{0}'".format(table_name))
columns = cursor.fetchall()

# Create List of columns not including Id and Geography
for column in columns[1:-1]:
    col_list.append(column[0])

for i in col_list:
    # Query for distinct lengths from table
    cursor.execute("SELECT DISTINCT LEN({0}) AS lth FROM {1};".format(i, table_name))
    rows = cursor.fetchall()
    allownull = False  # Set allownull to default value of false

    len_list = []  # Create empty list to hold length values of current column in loop

    print(i)  # Print current column
    txt_export.write(i + '\n')

    for row in rows:
        if row[0] is not None:  # Add len value to list if not NULL/None
            len_list.append(row[0])
        else:
            print("Has NULL")  # Inform user NULLs exist
            txt_export.write("Has NULL\n")
            allownull = True

    print("Min Char: ", min(len_list))
    txt_export.write("Min Char: {0}\n".format(min(len_list)))
    print("Max Char: ", max(len_list))
    txt_export.write("Max Char: {0}\n".format(max(len_list)))

    if min(len_list) == 0:  # Set all empty strings to NULL
        cursor.execute("UPDATE {0} SET {1} = NULL WHERE {1} = '';".format(table_name, i))
        print("Empty values in [{0}] set to NULL".format(i))
        txt_export.write("Empty values in [{0}] set to NULL\n".format(i))
    print("")  # Print an empty line
    txt_export.write("\n")  # Write an empty line to file

    cursor.execute("SELECT DISTINCT {0} FROM {1};".format(i, table_name))  # Retrieve distinct files from each column
    results = cursor.fetchall()  # Set list, results, to these distinct values

    for result in results:  # Write distinct values from each column to designated file
        txt_export.write("{0}\n".format(result[0]))
    txt_export.write("\n")  # Line separation between columns

cnxn.commit()  # Commit any Empty -> NULL changes
txt_export.close()
cursor.close()
cnxn.close()
