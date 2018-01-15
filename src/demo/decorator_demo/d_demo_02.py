def printdebug(func):
    def _decorater(user):
        print("enter the login")
        result = func(user)
        print("exit the login")
        return result
    return _decorater

@printdebug
def login(user):
    print("in login ", user)
    msg = "success" if user == "jatsz" else "fail"
    return msg

ll = login("daijitao")
print(ll)