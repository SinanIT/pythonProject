class CustomException(Exception):
    pass
def causeError():
    raise CustomException('You called the cause error funtion')
#causeError() # __main__.CustomException: You called the cause error funtion

# Adding Attributes

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Recourse not Found!'

def raiseNotFoundError():
    raise NotFound()  #NotFound: Status code: 404 and message is: Recourse not Found!

raiseNotFoundError()
class ServerError(HttpException):
    statusCode = 500
    message = 'This server messed up!'

def raiseServerError():
    raise ServerError()  # Status code: 500 and message is: This server messed up!

#raiseServerError()