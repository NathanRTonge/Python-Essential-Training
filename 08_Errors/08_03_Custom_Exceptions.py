"""
This contains info on making custom exceptions
"""

class CustomException(Exception):
    pass #needs little adding to, inherits Exception attributes

def causeError():
    raise CustomException('You called the causeError function'
                          ' which is a custom error we made.')

"""Adding Attributes"""

class HttpException(Exception):
    statusCode= None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} & '
                         f'message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up'

def raiseServerError():
    raise ServerError

# Custom exceptions keeps code clean, organised and documented
# also seperate common errors from those that need dev attention

# please chose which error you would like to see
raiseServerError()
#causeError()
