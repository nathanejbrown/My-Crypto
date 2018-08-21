# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

# 2) Use the datetime library together with the random number to generate a random, unique value.

import random
import datetime

print(random.random())
rando = random.randint(1, 10)

print(str(rando) + str(datetime.datetime.now()))

year = random.randint(1950, 2000)
month = random.randint(1, 12)
day = random.randint(1, 28)
hour = random.randint(0, 23)
minute = random.randint(0, 59)
second = random.randint(0, 59)
print(datetime.datetime(year, month, day, hour, minute, second))

