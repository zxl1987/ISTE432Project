from Data.DB import *
from Data.userInfo import *
import re
getDB=Database()
userInfo=userInformation()


def verify(username, password):
    verifyUser=getDB.authUser(username, password);
    if verifyUser:
        userInfo.setUserid(verifyUser[0][0])
        return True
    else:
        return False


def signUp(username, password):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if ' ' in username or ' ' in password:
        return "User name or password can't contain the space"
    elif (regex.search(username) != None):
        return "User name can't contain the special charater"
    elif getDB.verifyUser(username):
        return  "Username already exists please try another one."
    
    getDB.setUser(username, password)
    return True
if __name__ == '__main__':
    verify("fenglin", "password")
