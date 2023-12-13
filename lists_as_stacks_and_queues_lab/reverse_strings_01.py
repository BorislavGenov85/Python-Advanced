# first solution

string = input().split()
text = []

for i in range(len(string) - 1, -1, -1):
    word = string[i][::-1]
    text.append(word)
    string.pop()

print(" ".join(text))

# second solution

# text = [x for x in input()]
# new_text = []
#
# while text:
#     ch = text.pop()
#
#     new_text.append(ch)
#
# print(*new_text, sep="")
