
class ContextManager(object):
    def __init__(self):
        self.entered = False
        print('init runs')
    def __enter__(self):
        self.entered = True
        print('enter runs')
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False
        print('exit')

with ContextManager() as c:
    c.enterd

class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(Single, cls)
            cls._instace = origin.__new__(cls, *args, **kwargs)
        return cls._instace