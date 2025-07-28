studentArr = [
    {
        "name": "Muthu",
        "gender": "M",
        "marks": {"kannada": 82, "english": 74, "maths": 88, "science": 72, "social": 90}
    },
    {
        "name": "Arun",
        "gender": "M",
        "marks": {"kannada": 78, "english": 59, "maths": 79, "science": 99, "social": 82}
    },
    {
        "name": "Abi",
        "gender": "F",
        "marks": {"kannada": 98, "english": 94, "maths": 82, "science": 72, "social": 86}
    },
    {
        "name": "Chitra",
        "gender": "F",
        "marks": {"kannada": 57, "english": 35, "maths": 48, "science": 32, "social": 35}
    },
    {
        "name": "Saravanan",
        "gender": "M",
        "marks": {"kannada": 97, "english": 91, "maths": 92, "science": 83, "social": 79}
    },
    {
        "name": "Sathish",
        "gender": "M",
        "marks": {"kannada": 32, "english": 36, "maths": 31, "science": 39, "social": 44}
    }
]

# ---------------- Functional Analytics ----------------

def get_total_marks(student):
    return sum(student['marks'].values())

def get_average(student):
    return get_total_marks(student) / len(student['marks'])

def get_result(student):
    return 'Pass' if all(mark >= 35 for mark in student['marks'].values()) else 'Fail'

def get_all_std_avg(students):
    return [round(get_average(s), 2) for s in students]

def get_gender_avg(students, gender):
    gender_students = [s for s in students if s['gender'] == gender]
    if not gender_students:
        return 0
    return round(sum(get_average(s) for s in gender_students) / len(gender_students), 2)

def get_subject_avg(students, subject):
    return round(sum(s['marks'][subject] for s in students) / len(students), 2)

def get_overall_result(students):
    return [{'name': s['name'], 'result': get_result(s)} for s in students]

def get_pass_count(students):
    return sum(1 for s in students if get_result(s) == 'Pass')

def get_fail_count(students):
    return sum(1 for s in students if get_result(s) == 'Fail')

def get_pass_list(students):
    return [s['name'] for s in students if get_result(s) == 'Pass']

def get_fail_list(students):
    return [s['name'] for s in students if get_result(s) == 'Fail']

def get_result_by_name(students):
    return {s['name']: get_result(s) for s in students}

# ---------------- Call and Print ----------------

print("All Student Averages:", get_all_std_avg(studentArr))
print("Male Average:", get_gender_avg(studentArr, 'M'))
print("Female Average:", get_gender_avg(studentArr, 'F'))
print("Kannada Average:", get_subject_avg(studentArr, 'kannada'))
print("English Average:", get_subject_avg(studentArr, 'english'))
print("Overall Result:", get_overall_result(studentArr))
print("Pass Count:", get_pass_count(studentArr))
print("Pass List:", get_pass_list(studentArr))
print("Fail Count:", get_fail_count(studentArr))
print("Fail List:", get_fail_list(studentArr))
print("Result by Name:", get_result_by_name(studentArr))
