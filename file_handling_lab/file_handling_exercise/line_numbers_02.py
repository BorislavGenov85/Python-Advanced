import string

with open("line_numbers.txt", "r") as input_line, open("output_line_numbers.txt", "w") as output_file:

    for line_number, line in enumerate(input_line, 1):
        line = line.strip()  # Remove leading/trailing whitespace
        line_length = sum([len(x) for x in line if x != " "])  # Character count
        punctuation_count = sum(line.count(char) for char in string.punctuation)  # Punctuation mark count

        correct_line = f"Line {line_number}: {line} ({line_length - punctuation_count})({punctuation_count})\n"
        output_file.write(correct_line)
