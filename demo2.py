def divide_students():
    studentsList = ["Matthew","Joshua","Ali","Betty","Simon","Kurtz","Didem","Freddy","Furkan"]
    newStudentList = [[],[]]
    for index, student in enumerate(studentsList):
        if index % 2 == 0:
            newStudentList[0].append(student)
        else:
            newStudentList[1].append(student)
    return newStudentList

print(divide_students())
