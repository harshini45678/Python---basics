students = [
    ["Harshini", 90, 95, 88],
    ["Keerthi", 85, 80, 92],
    ["Navya", 78, 89, 91]
]

for student in students:
    print(student[0])
    total = 0
    for mark in student[1:]:
        print(mark)
        total = total + mark
    
    average = total/3
  
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 7:
        grade = "C"
    else:
        grade = "D"

    print("Total :",total)
    print("Average :",average)
    print("Grade :", grade)