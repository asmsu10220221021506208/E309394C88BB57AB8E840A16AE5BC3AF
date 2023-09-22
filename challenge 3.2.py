class student:
  
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of the students in descending order of CGPA
  sorted_students = sorted(student_list, 
                           key=lambda student: student.cgpa,
                           reverse=True)
  #syntax - lambda arg:exp
  return sorted_students


# Example Usage:
students = [
  student("arshi", "A2415", 8.9),
  student("usa", "A2418", 8.6),
  student("fathima", "A2416",8.1),
  student("thasleema", "A2417", 8.2),
]

sorted_students = sort_students(students)

#print the sorted List of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name, 
                                                   student.roll_number,student.cgpa))