def movie_organizer(*args):
    movie_library = {}

    for item in args:
        name = item[0]
        genre = item[1]
        if genre not in movie_library:
            movie_library[genre] = []
        movie_library[genre].append(name)

    sorted_movie_library = sorted(movie_library.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for genre, movies in sorted_movie_library:
        sorted_names = sorted(movies)
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted_names:
            result += f"* {movie}\n"

    return result.strip()


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))