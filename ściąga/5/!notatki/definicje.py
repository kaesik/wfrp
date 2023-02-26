#definicje
def ask_for_the_name():
	name_def = ""
	while name_def == "":
		name_def = input("what is yor name? :")
	return name_def
def ask_for_the_age(person_name):
	age_int = 0
	while age_int == 0:
		age_str = input(person_name + " what is your age? :")
		try:
			age_int = int(age_str)
		except:
			print("EROOR: Age must be a number.")
	return age_int
def display_person_info (name, age):
	print("")
	print(f"your name is {name}, you are {age} years old")
	print("Soon you will be " + str(age + 1))

#ask for the name
name1 = ask_for_the_name()
name2 = ask_for_the_name()

#ask for the age
age1 = ask_for_the_age(name1)
age2 = ask_for_the_age(name2)

#display the results
display_person_info(name1,age1)
display_person_info(name2,age2)
