while True:
    number = input("Enter an integer: ")

    if number.isdigit():
        print("This is an integer.")
        break
    else:
        print("This is not an integer.")
        continue