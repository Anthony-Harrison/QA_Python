'''Takes a name and 3 ints
calculates the total of the 3 ints and produces a percentage and grade'''
def score(name, h, a, f):
    grade = ""
    fScore = round(((h + a + f) / 175) * 100)
    if fScore > 85:
        grade = "A"
    elif fScore >= 70:
        grade = "B"
    elif fScore >= 50:
        grade = "C"
    else:
        grade = "Fail"
    return name, fScore, grade

a = score("Anth", 25, 20, 100)
print(f"The values returned by the function score are {a}")
print(f"The student {a[0]} had a final score of {a[1]}%. \
Achieving a grade of {a[2]}.")
