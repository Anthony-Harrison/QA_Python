def score(name, h, a, f):
    fScore = round((((h/25) + (a/50) + (f/100)) / 3) * 100)
    return name, fScore

a = score("anth", 22,46,97)
print((f"The student {a[0]} had a final score of {a[1]}%."))
