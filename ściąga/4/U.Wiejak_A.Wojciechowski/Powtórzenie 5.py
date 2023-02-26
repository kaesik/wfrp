import random

a = random.randint(1, 2)
if a == 1:
	przedmiot = "długopis"
elif a == 2:
	przedmiot = "ołówek"

if przedmiot == "długopis":
	strona = "po prawej"
if przedmiot == "ołówek":
	strona = "po lewej"

print("wkładam "+przedmiot+" do pudełka "+strona)