def start_spring(**kwargs):
    collection = {}
    for name, info in kwargs.items():
        if info not in collection:
            collection[info] = []
        collection[info].append(name)

    collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))
    sorted_collection = {k: sorted(v) for k, v in collection}

    result = []
    for key, value in sorted_collection.items():
        result.append(f"{key}:")
        for el in value:
            result.append(f"-{el}")

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
