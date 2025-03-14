import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
ok = random.choice(friends)
# print(ok)

rindex = random.randint(0,4)
re  = friends[rindex]

if ok == re:
    print('equal match')
