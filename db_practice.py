import pymssql
db_usr = raw_input("please input username: \n")
db_pwd = raw_input("please input password: \n")

db_connect = pymssql.connect(
    server='grchilhq-sq-03',
    #port = 1433, # apparently this line was not needed; b/c port is default?
    user = db_usr,
    password = db_pwd,
    database = 'Analytics'
    )

my_cursor = db_connect.cursor()
my_cursor.execute('SELECT * FROM [Analytics].[dbo].[AppraiserPerformanceTest]')

row = my_cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = my_cursor.fetchone()

print("We're good, now we'll log off.")

db_connect.close()
