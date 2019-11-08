from Data.DB import *
from Data.userInfo import *
import re
getDB=Database()
userInfo=userInformation()


def verify(username, password):
    verifyUser=getDB.authUser(username, password);
    print verifyUser
    if verifyUser:
        userInfo.setUserid(verifyUser[0][0])
        return True
    else:
        return False


def signUp(username, password):
    if ' ' in username or ' ' in password:
        return "User name or password can't contain the space"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(username) != None):
        return "User name can't contain the special charater"
    if getDB.verifyUser(username):
        return "username already exists please try another one."
    if getDB.setUser(username, password):
        return "Account create successfully"
    else:
        return "Fail to create account"

if __name__ == '__main__':
    verify("fenglin", "password")
