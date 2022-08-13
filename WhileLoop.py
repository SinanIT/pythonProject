from datetime import datetime

print(datetime.now())  # 2022-08-12 21:14:32.905648

print(datetime.now().second)  # 11

wait_until = datetime.now().second + 2

# Pass
while datetime.now().second != wait_until:
    # print('Still waiting')
    pass
print(f'We are at {wait_until} seconds')

wait_until = datetime.now().second + 2

# Break
while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds')
        break
