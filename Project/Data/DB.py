import MySQLdb


class DB:
	try:
		db = MySQLdb.connect(host='localhost', user='root', passwd='student', db='weather')
		cur = db.cursor()
		cur.execute("select * from user;")
		result = cur.fetchall()
		print result
	except:
	    print("Service Downtime. Please try again later.")