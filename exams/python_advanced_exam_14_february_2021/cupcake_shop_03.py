def stock_availability(*args):

    boxes = args[0]
    command = args[1]

    if command == "delivery":
        products = args[2:]
        for product in products:
            boxes.append(product)

    elif command == "sell":
        parameters = args[2:]
        if not parameters:
            boxes.pop(0)

        elif isinstance(parameters[0], int):
            number = int(parameters[0])
            for _ in range(number):
                boxes.pop(0)

        else:
            for product in parameters:
                while product in boxes:
                    boxes.remove(product)

    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

