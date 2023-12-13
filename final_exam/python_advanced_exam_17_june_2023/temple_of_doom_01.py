from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while True:
    tool = tools[0]
    substance = substances[-1]
    result = tool * substance

    if result in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(result)

    else:
        tool = tools.popleft() + 1
        tools.append(tool)
        substance = substances.pop() - 1
        if substance > 0:
            substances.append(substance)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    if not tools or not substances and len(challenges) > 0:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break


if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
