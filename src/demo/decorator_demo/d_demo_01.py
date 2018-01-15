
def printdebug_1(func):
    print("in printdebug")
    func()
    print('exit printdebug')

def printdebug(func):
    def _decorater(user):
        print("enter the login")
        print(user)
        func(user)
        print("exit the login")
    return _decorater

def printdebug_level(level):
    def printdebug(func):
        def _decorater(user):
            print("enter the log , and debug level is ", str(level))
            func(user)
            print("exit the login , and leve is " + str(level))
        return _decorater
    return printdebug

@printdebug_level(level=2)
def login(user):
    print("in login ", user)


login("daijityao")