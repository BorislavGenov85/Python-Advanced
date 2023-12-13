words = open("words.txt", "r")
words_el = words.read().split()
words_el = [el.strip("\n") for el in words_el]

data = open("text.txt", "r")
data_el = data.read().split()
data_el = [el.lower().strip("-").strip(".").strip(",") for el in data_el]

matching_words = {}
for word in words_el:
    if word in data_el:
        num = data_el.count(word)
    matching_words[word] = num

sorted_matching_word = sorted(matching_words.items(), key=lambda x: x[1], reverse=True)

file = open("other_text_files.txt", "w")
for el in sorted_matching_word:
    file.write(f"{el[0]} - {el[1]}\n")
