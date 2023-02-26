import time
czas = time.gmtime()

sekundy = int(input("Podaj ile minęło sekund od pełnej minuty: "))

if sekundy == czas[5]:
	print("Gratulacje!")
else:
	print("Próbuj dalej.")