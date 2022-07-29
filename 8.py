
"""module"""
import math
import random
import statistics
import keyword

nums = [1, 3, 5, 7, 9, 0]

try:
	x = input('перше число: ')
	x = int(x)
	y = input('друге число: ')
	y = int(y)
	res = math.pow(x, y)
	res2 = random.randint(x, y)

except (ValueError, TypeError, NameError):
	print("Only integer")

try:
        print(res)
        print(res2)
        print(statistics.mean(nums))
        print(statistics.median(nums))
        print(statistics.mode(nums))
        print(keyword.iskeyword('math'))
        print(keyword.iskeyword('for'))
        print(keyword.iskeyword('and'))

except (NameError):
        print("restart program")

"""8.1"""
try:
	a = input('зп за січень: ')
	a = int(a)

	b = input('зп за лютий: ')
	b = int(b)

	c = input('зп за березень: ')
	c = int(c)

	d = input('зп за квітень: ')
	d = int(d)

	money = [a, b, c, d]
	
	print(statistics.mean(money))
	print(statistics.median_low(money))

except (ValueError, TypeError, NameError):
	print("Only integer")

"""8.2"""
import cubed
