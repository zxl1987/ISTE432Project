from DB import *
getDB=Database()
def test():
    print(getDB.setUser("fenglin123", "password"))


if __name__ == "__main__":
    test()