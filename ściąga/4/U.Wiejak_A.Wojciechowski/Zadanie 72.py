import random

a = random.randint(1, 100)
t = [a]
while len(t) < 11:
	b = random.randint(1, 100)
	t.append(b)

print(t)
b = 0
if t[b] > t[b+1]:
	print("Tablica jest nieposortowana, posortować?")
	print("y/n: ")
	odp =input()
	if odp == "y":
		t.sort()
		print("Posortowano.")
	else:
		print("Nie posortowano")

print(t)