student_details = ("harshini", "CSD", 20, "JBIET")
print(student_details)
print(student_details[0])
print(student_details[2])
student_info = ([("harshini"),("csd"),(20),("jbiet")])
print(student_info)
print(type(student_info))
print(type(student_details))
student_info[1] = "CSM" 
print(student_info)
print(len(student_details))
print(len(student_info))
print(student_details[1:3])
print(student_details.count(20))


fruits1 = ("apple", "banana", "muskmelon")
fruits2 = ("curstard apple", "watermelon", "kiwi", "mango")
fruits = fruits1 + fruits2
print(fruits) 