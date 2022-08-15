def causeError():
    return 1/0

def callCauseError():
    return causeError()

#callCauseError()

'''
Traceback (most recent call last):
  File "C:\\Users\sinan\PycharmProjects\pythonProject\ErrorsAnExceptions.py", line 7, in <module>
    callCauseError()
  File "C:\\Users\sinan\PycharmProjects\pythonProject\ErrorsAnExceptions.py", line 5, in callCauseError
    return causeError()
  File "C:\\Users\sinan\PycharmProjects\pythonProject\ErrorsAnExceptions.py", line 2, in causeError
    return 1/0
ZeroDivisionError: division by zero
'''

#Try Expect

try:
    1/0
except Exception as e:
    print(type(e)) # <class 'ZeroDivisionError'>
