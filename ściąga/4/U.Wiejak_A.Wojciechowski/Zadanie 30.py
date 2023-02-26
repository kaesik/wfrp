import time
a = int(time.time())
c = int(input("Podaj wynik mnożenia 5*5= "))
if c == 25:
	b = int(time.time())
	print("Dobrze, zajęło ci to " + str(b-a) + " sekund.")