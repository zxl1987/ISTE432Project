from DB import *
getDB=Database()
def test():
    '''
    print(getDB.setUser("fenglin123", "password", "meial@gmail"))
    print(getDB.verifyUser("fenglin123"))
    print(getDB.setUserInfo("1", "Feng", "Lin", "1996-12-18","Windish"))
    print(getDB.viewUserInfo(userId))
    print(getDB.updateInfo("1", "Feng", "Lin", "1996-07-06", "Wdish"))
    print(getDB.viewUserInfo(userId))
    '''
    userId="1"
    print(getDB.viewUserInfo(userId))
    print(getDB.getUserHistory(userId))
    print(getDB.setUserHistory(userId, 1, "Brookly"))
    print(getDB.getUserHistory(userId))
    print(getDB.setUserHistory(userId, 1, "19152"))
    print(getDB.getUserHistory(userId))

    print(getDB.deleteUserHistory(userId, "3"))
    print(getDB.getUserHistory(userId))


if __name__ == "__main__":
    test()