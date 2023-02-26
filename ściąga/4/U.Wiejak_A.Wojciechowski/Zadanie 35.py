punkty = 0

zadanie1 = int(input("Ile wynosi 3+3*3?\n-> "))
if zadanie1 == 12:
	punkty += 1
else:
	print("Zła odpowiedź!")
zadanie2 = input("Jakiego koloru jest biała ściana?\n-> ")
if zadanie2 == "biały":
	punkty += 1
else:
	print("Zła odpowiedź!")
zadanie3 = input("Co Henio robi?\n-> ")
if zadanie3 == "śmierdzi":
	punkty += 1
else:
	print("Zła odpowiedź!")
print("Udało ci się zdobyć")
if punkty == 0:
	print(punkty, " punktów.")
if punkty == 1:
	print(punkty, " punkt.")
if punkty == 2:
	print(punkty, " punkty.")
if punkty == 3:
	print(punkty, " punkty.")