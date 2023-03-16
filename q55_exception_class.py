class MyError(Exception):
    '''My custom exception class
    Attributes:
        msg -- explanation of the error
    '''
    def __init__(self,msg):
        self.msg = msg

error = MyError("something wrong")
print(error.msg)
raise error
