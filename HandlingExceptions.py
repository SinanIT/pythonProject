import time


def causeError():
    try:
        return 1 / 0
    except Exception as e:
        print(e)  # division by zero


causeError()


def causeError1():
    try:
        return 1 / 0
    except Exception as e:
        print('There was some sort of error!')  # There was some sort of error!


causeError1()


# Finally
def causeError2():
    try:
        return 1 / 0
    except Exception as e:
        print('There was some sort of error!')  # There was some sort of error!
    finally:
        print('This will always execute!')  # This will always execute!


causeError2()


# Timer
def causeError3():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1 / 0
    except Exception as e:
        print('There was some sort of error!')  # There was some sort of error!
    finally:
        print(
            f'Function took {time.time() - start} seconds to execute')  # Function took 0.5015037059783936 seconds to execute


causeError3()


# Exception catching by type. Specific exception ones should be at up
def causeError4():
    try:
        return 1 / 0
    except TypeError:
        print('There was a type error')
    except ZeroDivisionError:
        print('There was a zero devision error!')  # There was a zero devision error!
    except Exception:
        print('There was some sort of error!')


causeError4()


# CustomDecorators
def handleException(func):
    def wrapper():
        try:
            func()
        except TypeError:
            print('There was a type error')
        except ZeroDivisionError:
            print('There was a zero devision error!')  # There was a zero devision error!
        except Exception:
            print('There was some sort of error!')

    return wrapper


@handleException
def causeError():
    return 1 / 0


causeError()


# Rasing Exceptions

@handleException
def raiseError():
    raise Exception


raiseError()  # There was some sort of error!


def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error')
        except ZeroDivisionError:
            print('There was a zero devision error!')  # There was a zero devision error!
        except Exception:
            print('There was some sort of error!')

    return wrapper


@handleException
def raiseError(n):
    if n == 0:
        raise Exception
    print(n)


raiseError(1)  # 1
