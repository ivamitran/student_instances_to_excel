import openpyxlForMain
import os

class student:
    def __init__(self, id, firstName, lastName, grade, gpa):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
        self.gpa = gpa


studentList = []
id = 0

def studentCreator():
    global id
    currentId = id
    firstName = input("Enter the first name of the student: ")
    lastName = input("Enter the last name of the student: ")
    grade = input("Enter the grade of the student: ")
    gpa = input("Enter the gpa of the student: ")
    id = id + 1

    return student(currentId, firstName, lastName, grade, gpa)


def mainFunction():
    print(
        "Actions: [1] Add Student, [2] Remove Student, [3] Create Excel File, [4] Exit Program"
    )
    response = input(
        "What action would you like to perform (Enter corresponding number): "
    )

    if str(response) == "1":
        currentStudent = studentCreator()
        studentList.append(currentStudent)
        print("Successfully added " + currentStudent.firstName + ".")

    
    if str(response) == "3":
        openpyxlForMain.createExcelFile()
        os.open('studentsExcelSheet.xlsx')

    
    if str(response) == "4":
        print("Program Ending...")
        global x
        x = 2


def repeat():
    while x == 1:
        mainFunction()


repeat()

# Test
