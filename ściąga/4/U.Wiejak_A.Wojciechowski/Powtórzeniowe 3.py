import time

czas = time.gmtime()
if czas[6] != 4:
	print("Byle do piątku!")
if czas[6] == 4:
	print("Piątek, piąteczek, piątunio!")