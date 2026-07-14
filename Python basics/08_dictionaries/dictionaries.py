student_info = {
    "Name" : "Harshini",
    "Roll no" : 246756701,
    "Branch" : "CSD",
    "Mobile no" : 6301983690,
    "CGPA" : 8.85
}

print(student_info)
print(student_info.keys())
print(student_info.values())

emp_info = {
    "name" : "lilly",
    "role" : "tester",
    "salary" : 50000
}

stud_emp_info = student_info.copy()
stud_emp_info.update(emp_info)
print(stud_emp_info)
