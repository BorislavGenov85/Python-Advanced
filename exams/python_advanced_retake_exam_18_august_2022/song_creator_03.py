def add_songs(*args):
    result = {}
    for name, items in args:
        if name not in result:
            result[name] = []
        for item in items:
            result[name].append(item)
    info = []
    for title, lyrics in result.items():
        info.append(f"- {title}")
        for lyric in lyrics:
            info.append(f"{lyric}")
    return "\n".join(info)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
