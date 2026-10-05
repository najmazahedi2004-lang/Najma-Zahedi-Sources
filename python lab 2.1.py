while True:
    x = input("Enter your mark: ")

    if x.isdigit():
        x = int(x)
        break
    else:
        print("Please enter an integer.")

if x >= 97 and x <= 100:
    print("A+")
elif x >= 93 and x <= 96:
    print("A")
elif x >= 90 and x <= 92:
    print("A-")
elif x >= 86 and x <= 88:
    print("B+")
else:
    print("No grade assigned")