# def gather_credits(needed_credits, *courses):
#
#     enrolled_course = []
#     total_credits = 0
#
#     for name, credit in courses:
#         if name not in enrolled_course and total_credits < needed_credits:
#             enrolled_course.append(name)
#             total_credits += int(credit)
#
#         if total_credits >= needed_credits:
#             break
#
#     if total_credits >= needed_credits:
#         return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(enrolled_course))}"
#     else:
#         return f"You need to enroll in more courses! You have to gather {needed_credits - total_credits} credits more."
#
#
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))


def gather_credits(*args):
    needed_credits = args[0]
    course_info = list(args[1:])
    enrolled_course = []
    total_credits = 0

    for course in course_info:
        name = course[0]
        credit = int(course[1])

        if name not in enrolled_course and total_credits < needed_credits:
            enrolled_course.append(name)
            total_credits += credit

        if total_credits >= needed_credits:
            break

    if total_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(enrolled_course))}"
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credits - total_credits} credits more."
