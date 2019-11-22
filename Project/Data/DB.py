import psycopg2
conn = None
class Database:
	def connect(self):
		try:
			conn = psycopg2.connect(host='localhost', database='userinfo', port="1996", user='postgres',
									password='student')
			return conn
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			conn.close()
	'''
	def connect(self):
		try:
			conn = psycopg2.connect(host='localhost', database='userinfo', port = "5432", user="user1", password="password1")
			return conn
		except (Exception, psycopg2.DatabaseError) as error:
			conn.close()
	'''
	def authUser(self, username, password):
		conn=self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select user_id from users where username='"+username+"' and password='"+password+"';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			return False
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
			return False
		finally:
			cur.close()
			conn.close()

	def setUser(self, username, password, email):
		query="INSERT INTO users (username, password ,email) VALUES (%s,%s,%s);"
		args=(username, password, email)
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute(query, args)
			conn.commit()
			return True
		except (Exception, psycopg2.DatabaseError) as error:
			return False
		finally:
			cur.close()
			conn.close()

	def viewUserInfo(self, userId):
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select * from information where user_id='" + userId + "';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			return False
		finally:
			cur.close()
			conn.close()

	def setUserInfo (self, userId, firstname, lastname, birth, address):
		query="INSERT INTO information (user_id, firstname, lastname ,birth, address) VALUES (%s,%s,%s,%s,%s);"
		args=(userId, firstname, lastname, birth, address)
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute(query, args)
			conn.commit()
			return True
		except (Exception, psycopg2.DatabaseError) as error:
			print error
			return False
		finally:
			cur.close()
			conn.close()

	def updateInfo(self, userId, firstname, lastname, birth, address):
		query = "Update information set firstname = %s, lastname = %s, birth = %s, address = %s where user_id = %s"
		args=(firstname, lastname, birth, address, userId)
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute(query, args)
			conn.commit()
			return True
		except (Exception, psycopg2.DatabaseError) as error:
			print error
			return False
		finally:
			cur.close()
			conn.close()

