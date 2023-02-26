import random
a = random.randint(1, 10)
t = [a]
b = 2

while len(t) != 5:
	t.append(a * b)
	b += 1

random.shuffle(t)
c = 0
while c < len(t)-1:
	print(t[c])
	c += 1

d = int(input("Jaka jest brakująca liczba?\n-> "))

if d == t[len(t)-1]:
	print("Dobrze!")
else:
	print("Źle!")