import psycopg2
conn = None
class Database:
	def connect(self):
		try:

			conn = psycopg2.connect(host='localhost', database='userinfo', port="1996", user='postgres',password='student')
			'''
			conn = psycopg2.connect(host='localhost', database='userinfo', port = "5432", user="user1", password="password1")
			'''
			return conn
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			conn.close()

	def authUser(self, username, password):
		conn=self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select user_id, password from users where username='"+username+"';")
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
		query="INSERT INTO users (username, password, email) VALUES (%s,%s,%s);"
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

	def changeEmail(self, newE, userId):
		query = "Update users set email = %s where user_id = %s;"
		args = (newE, userId)
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

	def getUserpassword(self, userId):
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select password from users where user_id='" + userId + "';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			return False
		finally:
			cur.close()
			conn.close()

	def updateUserPassword(self, userId, newP):
		query = "Update users set password = %s where user_id = %s;"
		args = (newP, userId)
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

	def getUserEmail(self,userId):
		conn=self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select email from users where user_id='" + userId + "';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			return False
		finally:
			cur.close()
			conn.close()

	def getUserHistory(self, userId):
		conn = self.connect()
		try:
			cur = conn.cursor()
			cur.execute("select * from history where user_id='" + userId + "';")
			result = cur.fetchall()
			return result
		except (Exception, psycopg2.DatabaseError) as error:
			return False
		finally:
			cur.close()
			conn.close()

	def setUserHistory(self, userId, type, location):
		query = "INSERT INTO history (user_id, local_type, address) VALUES (%s,%s,%s);"
		args = (userId, type, location)
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

	def deleteUserHistory(self, userId):
		query = "DELETE FROM history where user_id = %s;"
		args = (userId)
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

	


