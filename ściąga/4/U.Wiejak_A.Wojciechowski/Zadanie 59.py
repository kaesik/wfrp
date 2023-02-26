import time

a = int(input("Wpisz liczbę do odliczenia: "))
while a != 0:
	print(a)
	a -= 1
	time.sleep(1)
print("Koniec!")