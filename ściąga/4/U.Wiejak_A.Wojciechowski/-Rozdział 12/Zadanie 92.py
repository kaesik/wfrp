import random
t = []

for x in range(1,11):
	t.append(random.randint(1,100))
t1 = t[:5]
t2 = t[-5:]
print(t)
print(t1, t2)
if sum(t1) > sum(t2):
	print("Suma pierwszej połowy jest większa!")
elif sum(t2) > sum(t1):
	print("Suma drugiej połowy jest większa!")
elif sum(t2) == sum(t1):
	print("Niesamowite, są równe!")
else:
	print("Błąd!")