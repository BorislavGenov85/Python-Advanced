from collections import deque

file = open("even_lines_text", "r")
file_els = file.readlines()
file_el = [file_els[x] for x in range(len(file_els)) if x % 2 == 0]
character_to_be_replaced = {"-", ",", ".", "!", "?"}

result = []
for el in file_el:
    for symbols in character_to_be_replaced:
        if symbols in el:
            el = el.replace(symbols, "@")

    result.append(el)

reversed_el_result = []
for el in result:
    current_text = deque([])
    for word in el.split():
        word = word.strip("\n")
        current_text.appendleft(word)

    reversed_el_result.append(" ".join(current_text))
[print(x) for x in reversed_el_result]
