class Student:
    def __init__(self, name, age ,classs):
        self.name = name
        self.age = age
        self.classs = classs
    def avgTest(self, a, b, c):
        avg = (a + b + c) /3

        return avg


anth = Student("Anth", 31, "History" )
te = anth.avgTest(57,23,22)

print(f"assigned to variable > {te}%, Ran in print statement > \
{anth.avgTest(57,23,22)}% in {anth.classs}.")
print(type(anth))