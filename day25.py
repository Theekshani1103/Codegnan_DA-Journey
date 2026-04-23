class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(human):
    def __init__(self, name, age, student_id):
        human.__init__(self, name, age)
        self.student_id = student_id
        self.course = []

    def add_course(self, course_name):
        self.course.append(course_name)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)
        print("Course:", self.course)

class Professor(human):
    def __init__(self, name, age, emp_id):
        human.__init__(self, name, age)
        self.emp_id = emp_id
        self.course = []

    def add_course(self, course_name):
        self.course.append(course_name)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Course Teaching:", self.course)

st1 = Student("Theeku", 22, 2911)
st2 = Student("Janu", 22, 1911)
st1.add_course("Data Analytics")
st2.add_course("PFS")
print("Student details")
st1.display()
st2.display()
p1 = Professor("lalli", 35, "P500")
p2 = Professor("sreeja", 37, "P501")
print("professor details")
p1.display()
p2.display()








 




        

