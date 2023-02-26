print("Wypisz swoje ulubione filmy, jeżeli uznasz, że to wszystko napisz 'Koniec'")

t = [input()]
while t[len(t)-1] != "Koniec":
	t.append(input())
a = 0
while a < len(t)-1:
	print(t[a])
	a += 1