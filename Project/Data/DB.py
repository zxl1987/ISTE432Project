import psycopg2

class Database:
	conn=None
	def connect(self):
		try:
			conn = psycopg2.connect(host='localhost', database='userinfo', port = "1996", user='postgres', password='student')
			return conn
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			conn.close()

	def authUser(self, username, password):
		conn=self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select user_id from users where username='"+username+"' and password='"+password+"';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
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
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
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
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			return False
		finally:
			cur.close()
			conn.close()

