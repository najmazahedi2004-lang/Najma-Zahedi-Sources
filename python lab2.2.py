marks = [50, -100, -90, 200, 70, 99, 98, 86]

for mark in marks:
    if mark < 0 or mark > 100:
        print(mark, "is invalid")
    elif mark >= 97 and mark <= 100:
        print(mark, "A+")
    elif mark >= 93 and mark <= 96:
        print(mark, "A")
    elif mark >= 90 and mark <= 92:
        print(mark, "A-")
    elif mark >= 86 and mark <= 88:
        print(mark, "B+")
    else:
        print(mark, "No grade assigned")