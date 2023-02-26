import random

t = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
t2 = [[], [], [], [], []]
a = 0
while a < 5:
	b = 0
	while b < 5:
		t2[a].append(t[random.randint(1, 9)])
		b += 1
	a += 1
a = 0
while a < 5:
	print(t2[a][0], t2[a][1], t2[a][2], t2[a][3], t2[a][4])
	a += 1