class Student:
    def __init__(self, name, age ,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []

    def addStudent(self,student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        return False
    
    def getAverageGrade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)
    



s1 = Student("Anth", 31, 95)
s2 = Student("Bob", 25, 40)
s3 = Student("Eric", 27, 78)

course = Course("Science", 2)
course.addStudent(s1)
course.addStudent(s2)
print(course.getAverageGrade())