employeeArr = [
    {
        "name": "Ram",
        "gender": "M",
        "department": "Sales",
        "salary": 55000,
        "experience": 4
    },
    {
        "name": "Sita",
        "gender": "F",
        "department": "HR",
        "salary": 48000,
        "experience": 3
    },
    {
        "name": "John",
        "gender": "M",
        "department": "Engineering",
        "salary": 75000,
        "experience": 6
    },
    {
        "name": "Anjali",
        "gender": "F",
        "department": "Engineering",
        "salary": 70000,
        "experience": 5
    },
    {
        "name": "Karthik",
        "gender": "M",
        "department": "Sales",
        "salary": 52000,
        "experience": 2
    },
    {
        "name": "Meena",
        "gender": "F",
        "department": "HR",
        "salary": 47000,
        "experience": 1
    }
]


def get_total_salary(emp_list):
    return sum(emp["salary"] for emp in emp_list)

def get_average_salary(emp_list):
    return round(get_total_salary(emp_list) / len(emp_list),2)

def get_department_wise_avg(emp_list):
    dept_salary = {}
    dept_count = {}

    for emp in emp_list:
        dept = emp["department"]
        dept_salary[dept] = dept_salary.get(dept, 0) + emp["salary"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

    return {dept: dept_salary[dept]/dept_count[dept] for dept in dept_salary}

def get_gender_count(emp_list):
    male = sum(1 for emp in emp_list if emp["gender"] == "M")
    female = sum(1 for emp in emp_list if emp["gender"] == "F")
    return {"Male": male, "Female": female}

def get_experienced_employees(emp_list, min_years=5):
    return [emp["name"] for emp in emp_list if emp["experience"] >= min_years]

def get_department_employees(emp_list, dept_name):
    return [emp["name"] for emp in emp_list if emp["department"] == dept_name]

def get_highest_paid(emp_list):
    highest = max(emp_list, key=lambda x: x["salary"])
    return highest["name"], highest["salary"]

def get_salary_by_name(emp_list, name):
    for emp in emp_list:
        if emp["name"].lower() == name.lower():
            return emp["salary"]
    return "Employee not found"


print("Total Salary:", get_total_salary(employeeArr))
print("Average Salary:", get_average_salary(employeeArr))
print("Department-wise Average Salary:", get_department_wise_avg(employeeArr))
print("Gender Count:", get_gender_count(employeeArr))
print("Experienced Employees (5+ yrs):", get_experienced_employees(employeeArr))
print("Engineering Team:", get_department_employees(employeeArr, "Engineering"))
print("Highest Paid Employee:", get_highest_paid(employeeArr))
print("Salary of 'John':", get_salary_by_name(employeeArr, "John"))
print("Salary of 'Karthik':", get_salary_by_name(employeeArr, "Karthik"))
