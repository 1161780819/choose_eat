import MySQLdb

db = MySQLdb.connect("localhost","root","190011","yang")
cursor = db.cursor()

try:
    cursor.execute("select * from movie_info")
    data = cursor.fetchall()
    for i in data:
        for row in i:
            print row
except:
    print "error"