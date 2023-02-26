import random

a = input("kamień, papier, nożyce: ")
b = random.randint(1,3)

if b == 1:
	c = "kamień"
if b == 2:
	c = "papier"
if b == 3:
	c = "nożyce"

print("Komputer: ", c)

if a == "kamień":
	if b == 1:
		print("Remis!")
	if b == 2:
		print("Przegrałeś!")
	if b == 3:
		print("Wygrałeś!")
if a == "papier":
	if b == 1:
		print("Wygrałeś!")
	if b == 2:
		print("Remis!")
	if b == 3:
		print("Przegrałeś!")
if a == "nożyce":
	if b == 1:
		print("Przegrałeś!")
	if b == 2:
		print("Wygrałeś!")
	if b == 3:
		print("Remis!")