def students_credits(*args):
    total_credit = 0
    result = []

    for part in args:
        parts_info = part.split("-")
        course_name = parts_info[0]
        credit = int(parts_info[1])
        max_points = int(parts_info[2])
        diyan_points = int(parts_info[3])

        percentage_points = (diyan_points / max_points) * 100
        credit_he_has = (credit * percentage_points) / 100
        total_credit += credit_he_has

        result.append([course_name, credit_he_has])

    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    course_result = []
    if total_credit >= 240:
        course_result.append(f"Diyan gets a diploma with {total_credit:.1f} credits.")
        for name, points in sorted_result:
            course_result.append(f"{name} - {points:.1f}")
        return "\n".join(course_result)
    else:
        course_result.append(f"Diyan needs {240 - total_credit:.1f} credits more for a diploma.")
        for name, points in sorted_result:
            course_result.append(f"{name} - {points:.1f}")
        return "\n".join(course_result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
