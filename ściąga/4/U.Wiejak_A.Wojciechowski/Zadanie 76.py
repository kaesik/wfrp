import random
from progressbar import ProgressBar

bar = ProgressBar(maxval = 5)
bar.start()
punkty = 0
a = 1
print("Rozwiąż 10 prostych zadań, za każde dostaniesz 1 punkt:")
while a < 6:
	b = random.randint(1, 10)
	c = random.randint(1, 10)
	print("Zadanie " + str(a))
	print(str(b)+" + "+str(a)+" =")
	d = int(input())
	if d == b + c:
		print("Dobrze, dostajesz 1 punkt.")
		punkty += 1
	bar.update(punkty)
	a += 1
bar.finish()