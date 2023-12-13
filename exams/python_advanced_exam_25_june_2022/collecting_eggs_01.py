from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers = deque(int(x) for x  in input().split(", "))
box_size = 50
box_count = 0

while eggs and papers:
    egg = eggs[0]
    paper = papers[-1]

    if eggs[0] == 13:
        egg = eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    if egg <= 0:
        eggs.popleft()
        continue

    if egg + paper <= box_size:
        box_count += 1
        eggs.popleft()
        papers.pop()
    else:
        eggs.popleft()
        papers.pop()

if box_count > 0:
    print(f"Great! You filled {box_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")
