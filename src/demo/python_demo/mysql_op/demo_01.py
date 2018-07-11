

import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("./config.ini")
data = cf.sections()
host = cf.get(data[0], 'host')
print(data[0], 'host')
print(host)




def username(obj, _class):
    if isinstance(obj, _class):
        pass
