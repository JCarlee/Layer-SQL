# To Do
# Convert len(0) into NULL/None
# Export sample values into a file

import pyodbc

server = 'planet15.database.windows.net'
database = 'ugridd'
username = 'test'
password = 'Sql.123456'
driver = '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD=' +
                      password)
cursor = cnxn.cursor()


table_name = input('Type table name: ')  # Ask user for table name
print('')  # Print blank line

# Query to return all column names
cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{0}'".format(table_name))
rows = cursor.fetchall()

cursor.execute("SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{0}'".format(table_name))
datas = cursor.fetchall()

rowlist = []  # Create empty row list
typelist = []  # Create empty type list

# Create List of columns not including Id and Geography
for row in rows[1:-1]:
    rowlist.append(row[0])


for i in rowlist:
    # Query for distinct lengths from table
    cursor.execute("Select distinct LEN({0}) as lth from {1};".format(i, table_name))
    rows2 = cursor.fetchall()
    print(i)  # Print current column
    rowlist2 = []  # Create empty list
    allownull = False
    for row2 in rows2:
        if row2[0] is not None:  # Add len value to list if not NULL/None
            rowlist2.append(row2[0])
        else:
            print('Has NULL')  # Inform user NULLs exist
            allownull = True
    print('Min Char: ', min(rowlist2))
    print('Max Char: ', max(rowlist2), '\n')

cursor.close()
cnxn.close()
