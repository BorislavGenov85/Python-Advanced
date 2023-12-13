students_count = int(input())
students_data = {}
students_average = {}

for _ in range(students_count):
    name, grade = input().split()

    if name not in students_data:
        students_data[name] = []
    students_data[name].append(float(grade))

for name, grade in students_data.items():
    average_grade = f"{sum(grade) / len(grade):.2f}"
    students_average[name] = str(average_grade)

for name, grade in students_data.items():
    print(f"{name} -> ", end="")
    for num in grade:
        print(f"{num:.2f}", end=" ")
    print(f"(avg: {students_average[name]})")
