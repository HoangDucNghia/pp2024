def inputnumofstudent(numofstudent):
  numofstudent = int(input("Enter number of student:"))
  return numofstudent
def inputstudent(students):
  id = input("Enter student id:")
  name = input("Enter student name:")
  dob = input("Enter student date-of-birth:")
  students = {
      'id':id,
      'name':name,
      'dob':dob
  }
  return students
def inputnumofcourse(numofcourse):
  numofcourse = int(input("Enter number of courses:"))
  return numofcourse
def inputcourse(courses):
  course_id = input("Enter course id:")
  course_name = input("Enter course name:")
  courses={
      'course_id':course_id,
      'course_name':course_name
  }
  return courses
def select(students,course):
  print(f"Enter marks for student in course {inputnumofcourse.course_name}")
  marks = {}
  marks[course['course_id']] = []
  for student in students:
      mark=float(input(f"Enter mark for student {student['name']}"))
      studentmark = {
          'student_id':student['id'],
          'mark':mark
      }
      marks[course['course_id']] += [studentmark]
def showcourselist(courses):
  if (len(courses) == 0):
      print("The list is empty")
  else:
      print(f"{courses['course_id']} - {courses['course_name']}")
def showstudentlist(students):
  if (len(students) == 0):
      print("The list is empty")
  else:
      print(f"{students['id']} - {students['name']} - {students['dob']}")
def showmarks(marks,courses):
  for i in range(len(marks[courses['course_id']])):
      print(f"{marks[courses['course_id']][i]}")

def main():
  print("Student management system\n")
  print("-------------------------------------------------------------\n")
  print("Select:\n1.Enter number of student in a class\n2.Enter student information\n3.Enter number of courses\n4.Enter course information\n5.Enter mark\n6.List students\n7.List courses\n8.Show marks")
  print("-------------------------------------------------------------\n")
  courses={}
  students={}
  marks={}
  numofstudent=0
  numofcourse=0
  while(True):
      global s
      s=int(input("Select function:"))
      if(s==1):
         inputnumofstudent(numofstudent)
      elif(s==2):
         student = inputstudent(students)
         students[student['id']] = student
      elif(s==3):
         inputnumofcourse(numofcourse)
      elif(s==4):
         course = inputcourse(courses)
         courses[course["course_id"]] = course
      elif(s==5):
         select(students,courses)
      elif(s==6):
         showstudentlist(students)
      elif(s==7):
         showcourselist(courses)
      elif(s==8):
         showmarks(marks,courses)
      else:
         print("Error!Try again\n")
         s=int(input("Select function:"))
if __name__ == "__main__":
  main()