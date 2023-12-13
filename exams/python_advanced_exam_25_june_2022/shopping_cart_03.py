def shopping_cart(*args):
    max_products = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    meals_and_products = {"Soup": [], "Pizza": [], "Dessert": []}

    for item in args:
        if item == "Stop":
            break
        name = item[0]
        product = item[1]

        if product not in meals_and_products[name] and len(meals_and_products[name]) < max_products[name]:
            meals_and_products[name].append(product)

    sorted_meals = {k: v for k, v in sorted(meals_and_products.items(), key=lambda x: (-len(x[1]), x[0]))}

    if not sorted_meals["Soup"] and not sorted_meals["Pizza"] and not sorted_meals["Dessert"]:
        return "No products in the cart!"

    result = ""
    for meal, products in sorted_meals.items():
        if len(products) > 0:
            result += f"{meal}:\n"
            for prod in sorted(products):
                result += f" - {prod}\n"
        else:
            result += f"{meal}:\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
