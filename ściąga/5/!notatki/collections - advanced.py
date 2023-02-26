"""class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

pizzas = [
    Pizza("PEPPERONI", 9.99),
    Pizza("MARGARITA", 4.99),
    Pizza("HAWAI", 14.99)
]

pizzas_names = [i.name for i in pizzas if len(i.name) > 5]
print(pizzas_names)

#----- ANY -----
#return True if one item is True

expensive_pizza = any([i.price > 10 for i in pizzas])
print(expensive_pizza)
#----- SUM -----
#
expensive_pizza_nb = sum([1 for i in pizzas if i.price > 10])
print(expensive_pizza_nb)"""

pizza_names = ("pepperoni", "margarita", "hawai")
pizza_prices = (9.99, 4.99, 14.99)
names_and_prices = list(zip(pizza_names, pizza_prices))
for (name, price) in names_and_prices:
    print(f"{name} - {price}$")

#unzipped = list(zip(*names_and_prices))
pn, pp = list(zip(*names_and_prices))