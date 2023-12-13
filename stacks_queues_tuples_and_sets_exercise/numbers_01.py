first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
number = int(input())

for _ in range(number):
    line = input().split()
    command = line[0]
    sub_command = line[1]

    if command == "Add":
        if sub_command == "First":
            [first_sequence.add(int(x)) for x in line[2:]]
        else:
            [second_sequence.add(int(x)) for x in line[2:]]

    elif command == "Remove":
        if sub_command == "First":
            first_sequence = first_sequence.difference([int(x) for x in line[2:]])
        else:
            second_sequence = second_sequence.difference([int(x) for x in line[2:]])

    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
