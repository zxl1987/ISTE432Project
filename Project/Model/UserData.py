from Data.DB import *
from Data.userInfo import *
import re
getDB=Database()
userInfo=userInfo()
class UserData:

    def verify(self, username, password):
        verifyUser = getDB.authUser(username, password)
        if verifyUser:
            userInfo.setUserid(verifyUser[0][0])
            return True
        else:
            return False

    def signUp(self, username, password, email):
        print userInfo.getUserid()
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
        getDB.setUser(username, password, email)
        return True

    def vieUserInformation(self):
        return getDB.viewUserInfo(userInfo.getUserid())

    def setInformation(self, firstname, lastname, birth, address):
        if(getDB.viewUserInfo(userInfo.getUserid())):
            print "yest"
            getDB.updateInfo(userInfo.getUserid(), firstname, lastname, birth, address)
        else:
            print "no"
            getDB.setUserInfo(userInfo.getUserid(), firstname, lastname, birth, address)
