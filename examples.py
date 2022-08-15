nums = ['one', 'two', 'three']
s = " ".join(nums)
print(s)


def decor(func):
    def wrap():
        print('$$$$$')
        func()
        print('$$$$$')
    return wrap


@decor
def sayhi():
    print('hi')


sayhi()
