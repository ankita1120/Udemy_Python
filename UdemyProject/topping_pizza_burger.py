pizza_toppings = ['mushroom', 'olive', 'tomato', 'pepperoni', 'onion', 'garlic']
burger_toppings = ['lettuce', 'cheese', 'mayonnaise', 'bacon', 'pickle', 'avocado']

new_list = [topping for topping in pizza_toppings + burger_toppings if len(topping) > 5]
print(new_list)

