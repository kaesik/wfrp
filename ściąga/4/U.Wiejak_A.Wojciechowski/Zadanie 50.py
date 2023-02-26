import random

a = int(input("Podaj liczbę: "))
b = random.randint(1, 3)
if a == b:
	print("równe")
else:
	print("nierówne")