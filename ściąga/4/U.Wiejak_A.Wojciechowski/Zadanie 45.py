a = input("Podaj ciąg liter, sprawdze czy nie zawierają znaków specjalnych: ")

if a.find("!") or a.find("@") or a.find("#") or a.find("$"):
	print("Git")