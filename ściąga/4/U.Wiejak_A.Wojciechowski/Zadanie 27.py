import time
c = int(input("Podaj ile program ma czekać przed wyśmianiem cię: "))

if c > 10:
	print("Pokurwiło cię, nie będę tyle czekał!")
else:
	time.sleep(c)
	print("No i minęło, następuje wyśmianie: Ha-ha!")