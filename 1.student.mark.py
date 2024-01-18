numofstudent=0
numofcourse=0
def system():
    print("Student management system\n")
    print("-------------------------------------------------------------\n")
    print("Select:\n1.Enter number of student in a class\n2.Enter student information\n3.Enter number of courses\n4.Enter course information\n5.Enter mark\n6.List courses\n7.List students\n8.Show marks")
    print("-------------------------------------------------------------\n")
def inputnumofstudent():
    global numofstudent
    numofstudent = int(input("Enter number of student:"))
    return numofstudent
def inputstudent():
    id = input("Enter student id:")
    name = input("Enter student name:")
    dob = input("Enter student date-of-birth:")
    students = {
        "id":id,
        "name":name,
        "dob":dob
    }
    return students
def inputnumofcourse():
    global numofcourse
    numofcourse = int(input("Enter number of courses:"))
    return numofcourse
def inputcourse():
    course_id = input("Enter course id:")
    course_name = input("Enter course name:")
    course={
        "course_id":course_id,
        "course_name":course_name
    }
    return course
def select(students,course):
    print(f"Enter marks for student in course {inputnumofcourse.course_name}")
    marks = {}
    marks[course["id"]] = []
    for student in students:
        mark=float(input(f"Enter mark for student {student["name"]}"))
        studentmark = {
            "student_id":student["id"],
            "mark":mark
        }
        marks[course["id"]] += [studentmark]
def showcourselist(course):
    if (course.numofcourse == 0):
        print("The list is empty")
    else:
        print(course.course_id)
        print(course.course_name)
def showstudentlist(students):
    inputnumofstudent()
    inputstudent()
    if (students.numofstudent == 0):
        print("The list is empty")
    else:
        print(students.student_id)
        print(students.student_name)
def showmarks(select):
    print(select.marks)

def main():
    while(True):
        global s
        s=int(input("Select function:"))
        if(s==1):
           inputnumofstudent()
        elif(s==2):
           inputstudent()
        elif(s==3):
           inputnumofcourse()
        elif(s==4):
           inputcourse() 
        elif(s==5):
           select()
        elif(s==6):
           showstudentlist()
        elif(s==7):
           showcourselist()
        elif(s==8):
           showmarks()
        else:
           print("Error!Try again\n")
           s=int(input("Select function:"))
if __name__ == "__main__":
    main()



