def kwargs_length(**param):
    return len(param)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
