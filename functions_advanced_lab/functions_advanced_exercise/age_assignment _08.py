def age_assignment(*names, **name_and_age):
    result = []
    for name in names:
        if name[0] in name_and_age:
            result.append(f"{name} is {name_and_age[name[0]]} years old.")

    result = sorted(result, key=lambda x: x)
    return "\n".join(result)