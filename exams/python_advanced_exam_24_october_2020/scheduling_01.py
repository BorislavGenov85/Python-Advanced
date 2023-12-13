from sys import maxsize

jobs = [int(x) for x in input().split(", ")]
job_idx = int(input())

cycles_pass = 0

while jobs:
    current_cycle = min(jobs)

    idx = jobs.index(current_cycle)
    cycles_pass += current_cycle
    jobs[idx] = maxsize
    if idx == job_idx:
        break

print(cycles_pass)
