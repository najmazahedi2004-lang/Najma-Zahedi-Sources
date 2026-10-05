items = ["Apple", "banana", "Mango", "orange"]

item = input("Enter an item: ")

if item.lower() in [x.lower() for x in items]:  
    print("Available")
else:
    print("It is not available")
    items.append(item)

print("New list:", items)