persons = [
    ("Alice", 25, 1.6),
    ("Brian", 35, 1.8),
    ("Paul", 29, 1.7),
    ("Martin", 32, 1.7)
]

def get_infos(name, l):
    for i in l:
        if i[0] == name:
            return i
    return None

infos = get_infos("Paul", persons)

persons_dict = {
    "Alice": (25, 1.6),
    "Brian": (35, 1.8),
    "Paul": (29, 1.7),
    "Martin": (32, 1.7)
}

infos = persons_dict["Paul"]