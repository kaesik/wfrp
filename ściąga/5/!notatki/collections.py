# collection: arrays, lists, tuples....

#tuples: immutable - you cannot change it
#list: mutable - you can add/delete items or modify them

#TUPLES
"""            0       1       2       3
#persons = ("Brian", "Bob", "Alice", "Jean")

print(len(persons)) # 0 to len()-1
print(persons[-1]) # the last element

for i in range(0, len(persons)):
print(persons[i])"""

"""for i in persons:
    print(i)
    print(len(i))
    print(i[0])
    print()"""

"""values = range(0,5) # -> (0, 1, 2, 3, 4)"""

#LISTS
"""
persons = ["Brian", "Bob", "Alice", "Jean"]
new_person = "Dawid"
print(persons)
persons.append(new_person)
print(persons)
del persons[1]
print(persons)

def change_value(a):
    a[0] = 10

test = [1, 2, 3, 4]
print(test)
change_value(test)
print(test)"""

# TUPLES AND FUNCTIONS
"""def get_information():
    return "Alice", 20, 1.6

def display_information(name, age, heigh):
    print(f"Name: {name}, Age: {age}, Height: {heigh}")

infos = get_information()
print(infos)
display_information(*infos) # * rozpakowuje, czyli tworzy infos[0], infos[1], infos[2]"""

# SLICES

persons = ("Brian", "Bob", "Alice", "Jean", "Stefe", "Jon")
#print(persons)
#[start:stop:step] WAŻNE
for i in persons[0:2]:
    print(i)

name = "Alice"
print(name[0])