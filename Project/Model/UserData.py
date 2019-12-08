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
        signup = getDB.setUser(username, password, email)
        if signup:
            return True
        else:
            return False



    '''----------------------------------------------------------New Function-------------------------------------------------------------------------------------------------'''
    '''Get a list of User Information '''
    def viewUserInformation(self):
        return getDB.viewUserInfo(str(userInfo.getUserid()))

    '''Set the User Information'''
    def setInformation(self, firstname, lastname, birth, address):
        if birth=="":
            birth="Infinity"
        if getDB.viewUserInfo(str(userInfo.getUserid())):
            result = getDB.updateInfo(str(userInfo.getUserid()), firstname, lastname, birth, address)
        else:
            result = getDB.setUserInfo(str(userInfo.getUserid()), firstname, lastname, birth, address)
        return result

    '''Get a list of User History'''
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



    '''Delete a list of '''
    def deleteHisiotry(self):
        return getDB.deleteUserHistory(str(userInfo.getUserid()))

    @staticmethod
    def saveHistory(type, location):
        if userInfo.getUserid():
            return getDB.setUserHistory(str(userInfo.getUserid()), type, location)

    def getUserEmail(self):
        return getDB.getUserEmail(str(userInfo.getUserid()))

    def changeUserPassword(self, newP, oldP):
        print getDB.getUserpassword(str(userInfo.getUserid()))[0][0]
        if oldP != getDB.getUserpassword(str(userInfo.getUserid()))[0][0]:
            return False
        else:
            return getDB.updateUserPassword(str(userInfo.getUserid()), newP)

    def changeUserEmail(self, newE):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (not re.search(regex, newE)):
            return False
        return getDB.changeEmail(newE, str(userInfo.getUserid()))


