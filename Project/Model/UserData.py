from Data.DB import *
from Data.userInfo import *
import hashlib, binascii, os
import re
getDB=Database()
userInfo=userInfo()
class UserData:


    def verify(self, username, password):
        if getDB.authUser(username, self.hash_password(password)):
            verifyUser=getDB.authUser(username, self.hash_password(password))
            if self.verify_password(verifyUser[0][1], password):
                userInfo.setUserid(verifyUser[0][0])
                return True
            else:
                return False
        else:
            return False


    def signUp(self, username, password, email):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if ' ' in username or ' ' in password:
            return "User name or password can't contain the space"
        elif (regex.search(username) != None):
            return "User name can't contain the special charater"
        elif getDB.verifyUser(username):
            return "Username already exists please try another one."

        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (not re.search(regex, email)):
            return ("Invalid Email")
        signup = getDB.setUser(username, self.hash_password(password), email)
        if signup:
            return True
        else:
            return False

    def viewUserInformation(self):
        return getDB.viewUserInfo(str(userInfo.getUserid()))

    def setInformation(self, firstname, lastname, birth, address):
        if birth=="": birth="Infinity"
        if getDB.viewUserInfo(str(userInfo.getUserid())):
            result = getDB.updateInfo(str(userInfo.getUserid()), firstname, lastname, birth, address)
        else:
            result = getDB.setUserInfo(str(userInfo.getUserid()), firstname, lastname, birth, address)
        return result

    
    def viewUserHistory(self):
        historylist=[]
        if userInfo.getUserid():
            for a in getDB.getUserHistory(str(userInfo.getUserid())):
                historylist.append(a[3])
            return historylist

    def getOption(self, cityname):
        if userInfo.getUserid():
            for a in getDB.getUserHistory(str(userInfo.getUserid())):
                if a[3]==cityname:
                    return a[2]


    def deleteHisiotry(self):
        return getDB.deleteUserHistory(str(userInfo.getUserid()))

    @staticmethod
    def saveHistory(type, location):
        if userInfo.getUserid():
            return getDB.setUserHistory(str(userInfo.getUserid()), type, location)

    def getUserEmail(self):
        return getDB.getUserEmail(str(userInfo.getUserid()))

    def changeUserPassword(self, newP, oldP):
        if not self.verify_password(getDB.getUserpassword(str(userInfo.getUserid()))[0][0], oldP):
            print "heelo"
            return False
        else:
            return getDB.updateUserPassword(str(userInfo.getUserid()), self.hash_password(newP))

    def changeUserEmail(self, newE):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (not re.search(regex, newE)): return False
        return getDB.changeEmail(newE, str(userInfo.getUserid()))

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, password, userinput):
        """Verify a stored password against one provided by user"""
        salt = password[:64]
        stored_password = password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      userinput.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password