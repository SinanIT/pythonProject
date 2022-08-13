for n in range(1, 10):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print(('Fizz'))
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)

for n in range(1, 10):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
n = 5
print('**********************************')
# Ternary Operator
print('Fizz' if n % 3 == 0 else n)

fizzBuzz = 'Fizz' if n % 3 == 0 else n
print(fizzBuzz)

print('Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n)  # Buzz

print('FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n)  # Buzz
