from pizza_joint import Pizza

pizza_one = Pizza()

pizza_one.size = 16
pizza_one.style = "Thin & Crispy"
pizza_one.add_topping("Extra Cheese")
pizza_one.add_topping("Red Peppers")
pizza_one.print_order()




pizza_two = Pizza()

pizza_two.size = 18
pizza_two.style = "Deep Dish"
pizza_two.add_topping("Pepperoni")
pizza_two.add_topping("Sausage")
pizza_two.print_order()