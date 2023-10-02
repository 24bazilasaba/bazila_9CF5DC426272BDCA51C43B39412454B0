class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students

students=[
  Student("Saba","S001",3.9),
  Student("Shiza","S002",4.0),
  Student("Rufa","S003",4.0),
]
sorted_students=sort_students(students)

for Student in sorted_students:
  print(f"Name:{Student.name},Roll Number:{Student.roll_number}, CGPA:{Student.cgpa}")
