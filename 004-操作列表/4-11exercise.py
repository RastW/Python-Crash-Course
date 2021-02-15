pizzas = ['pepperoni pizza', 'mushroom ham pizza', 'potato pizza']
pizzas.append("checken pizza")
friend_pizzas = pizzas[:]
friend_pizzas.append("pork pizza")

for pizza in pizzas:
    print("My favorite pizzas are:" + pizza)

for pizza in friend_pizzas:
    print("My friend's favorite pizzasare:" + pizza)
