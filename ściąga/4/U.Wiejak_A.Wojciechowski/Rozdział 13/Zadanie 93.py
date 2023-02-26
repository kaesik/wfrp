file = open("93.txt", "r")
t = file.read().splitlines()
for x in t:
	print(x)
print("W pliku znajduje się tyle liczb: " + str(len(t)))
file.close()