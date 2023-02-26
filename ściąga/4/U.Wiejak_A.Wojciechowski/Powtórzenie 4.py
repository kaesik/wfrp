import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

print("Trzy losowe liczby to: ", a, ", ", b, " oraz ", c)
d = int(input("Podaj największą z podanych cyfr: "))

if d == a:
	if d >= b and d >= c:
		print("Dobra odpowiedź!")
	else:
		print("Zła odpowiedź!")
if d == b:
	if d >= a and d >= c:
		print("Dobra odpowiedź!")
	else:
		print("Zła odpowiedź!")
if d == c:
	if d >= b and d >= a:
		print("Dobra odpowiedź!")
	else:
		print("Zła odpowiedź!")
