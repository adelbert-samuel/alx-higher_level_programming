#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
phrase = "Last digit of"
if number > 0:
    result = number % 10
    if result > 5:
        print("{} {} is {} and is greater than 5".format(phrase, number, result))

    elif result == 0:
        print("{} {} is {} and is 0".format(phrase, number, result))

    elif result < 6:
        print("{} {} is {} and is less than 6 and not 0".format(phrase, number, result))

else:
    last = str(number)[-1]
    print("{} {} is -{} and is less than 6 and not 0".format(phrase, number, last))
