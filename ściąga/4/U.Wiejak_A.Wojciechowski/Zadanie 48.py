import random

a = random.randint(1, 10)
b = random.randint(1, 10)

c = random.randint(1, 4)

if c == 1:
	print(a, "+", b, "=", a+b)
elif c == 2:
	print(a, "-", b, "=", a-b)
elif c == 3:
	print(a, "*", b, "=", a*b)
else:
	print(a, "/", b, "=", a/b)