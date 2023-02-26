import random
import time

a = random.randint(0,100)
b = random.randint(0,100)
print("Ile wynosi ", a, "-", b, "?")
time1 = time.time()
c = int(input(": "))

if c == a - b:
	print("Dobra odpowiedź!")
	time2 = time.time()
	print("Zajęło ci to:", time2-time1)

else:
	print("Zła odpowiedź!")