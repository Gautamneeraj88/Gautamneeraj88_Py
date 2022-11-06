"""
9.Use dictionary to store marks of the students in 4 subjects.Write a function to
find the name of the student securing highest percentage.(Hint:Names of
students are unique).
"""
student = {}
def highest():
    a = -1
    for i in student:
        a = max(student[i], a)
    for i in student:
        if(student[i] == a):
            print("Name of the student: ",i, a)



number_of_student = int(input("Enter the number of students: "))
for i in range(number_of_student):
    name = input("Enter the name of student: ")
    var = 0.0
    for j in range(4):
        print("Enter the marks in subject ", j+1,": ")
        marks = float(input(""))
        var += marks
    var = var/4
    student[name] = var

highest()