def forecast(*args):
    sunny = []
    cloudy = []
    rainy = []
    for el in args:
        if el[1] == "Sunny":
            sunny.append([el[0], el[1]])
        elif el[1] == "Rainy":
            rainy.append([el[0], el[1]])
        else:
            cloudy.append([el[0], el[1]])

    result = []
    result += sorted(sunny) + sorted(cloudy) + sorted(rainy)

    town_forecast = []
    for name, info in result:
        town_forecast.append(f"{name} - {info}")

    return "\n".join(town_forecast)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))