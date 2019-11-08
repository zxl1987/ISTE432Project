import mysql.connector
from mysql.connector import Error

class Database:
	def connect(self):
		try:
			conn = mysql.connector.connect(host='localhost', database='userInfor', user='root', password='student')
			if conn.is_connected():
				return conn
		except Error as e:
			print(e)
			conn.close()

	def authUser(self, username, password):
		conn=self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select user_id from users where username='"+username+"' and password='"+password+"';")
			result = cur.fetchall()
			return result
		except Error as e:
			print(e)
		finally:
			cur.close()
			conn.close()

	def verifyUser(self, username):
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select * from users where username='" + username + "';")
			result = cur.fetchall()
			return result
		except Error as e:
			print(e)
		finally:
			cur.close()
			conn.close()


	def setUser(self, username, password):
		query="INSERT INTO users (username, password) VALUES (%s,%s);"
		args=(username, password)
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute(query, args)
			conn.commit()
			return True
		except Error as e:
			print(e)
			return False
		finally:
			cur.close()
			conn.close()

