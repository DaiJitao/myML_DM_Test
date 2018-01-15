
#多个装饰器
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator

def others(func):    #define a other decorator
    def __decorator():
        print('***other decorator***')
        func()
    return __decorator

@others  # apply two of decorator
@printdebug
def login():
    print('in login:')

@printdebug  # switch decorator order
@others
def logout():
    print('in logout:')

print('---------------------------')
logout()