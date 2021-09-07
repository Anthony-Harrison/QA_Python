def score(name, h, a, f):
    grade = ""
    fScore = round((((h/25) + (a/50) + (f/100)) / 3) * 100)
    if fScore > 85:
        grade = "A"
    elif fScore >= 70:
        grade = "B"
    elif fScore >= 50:
        grade = "C"
    else:
        grade = "Fail"
    return name, fScore, grade

a = score("anth", 22,46,97)
print((f"The student {a[0]} had a final score of {a[1]}%. \
Achieving a grade of {a[2]}."))
