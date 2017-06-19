# Import Bing Credentials
#
import pymssql #change to mysql
import credentials_page

db_connect = pymssql.connect(
    server = credentials_page.database_server,
    user = credentials_page.database_username,
    password = credentials_page.database_password,
    database = credentials_page.database_name
    )

external_SQL_file = open('agent_id_query.sql','r')
sql_script = external_SQL_file.read()
external_SQL_file.close()

my_cursor = db_connect.cursor()
my_cursor.execute(sql_script)

requested_values = []
row = my_cursor.fetchone()
while row:
    requested_values.append(row[0])
    row = my_cursor.fetchone() #without this, an infinite loop on the first row (why?)

#print requested_values

db_connect.close()
