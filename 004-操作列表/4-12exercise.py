# 4-12 使用多个循环：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表都打印出来。

pizzas = ['pepperoni pizza', 'mushroom ham pizza', 'potato pizza']
pizzas.append("checken pizza")
friend_pizzas = pizzas[:]
friend_pizzas.append("pork pizza")

for pizza in pizzas:
    print("My favorite pizzas are:" + pizza)

for pizza in friend_pizzas:
    print("My friend's favorite pizzasare:" + pizza)
